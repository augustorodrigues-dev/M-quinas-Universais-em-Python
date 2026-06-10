# -*- coding: utf-8 -*-
"""Autômato de Pilha (Pushdown Automaton) por pilha vazia para a linguagem
das sequências balanceadas de três tipos de delimitadores: (), [] e {}.

Modelo formal implementado:
    P = (Q, Σ, Γ, δ, q0, $, F)
    Q  = {q_inicio, q_lendo_paren, q_lendo_colch, q_lendo_chave,
          q_fechando_paren, q_fechando_colch, q_fechando_chave,
          q_aceita, q_rejeita}                         (9 estados)
    Σ  = { (, ), [, ], {, } }                          (alfabeto de entrada)
    Γ  = { $, (, [, { }                                (alfabeto de pilha; $ = fundo)
    q0 = q_inicio
    F  = {q_aceita}
    δ  : Q × (Σ ∪ {#}) × Γ → Q × Γ*   (# = fim de entrada lido apenas internamente)

Decisão de modelagem: um reconhecedor mínimo precisaria de um único estado de
controle, pois a decisão de aceitar/rejeitar é tomada pela pilha. Optou-se por
enriquecer o controle finito para que o estado registre o TIPO da última operação
(qual delimitador foi aberto/fechado por último). Isso torna o rastreamento de
execução autoexplicativo e evidencia, de forma didática, que estado e pilha são
componentes independentes do modelo — sem alterar a linguagem reconhecida.
"""


class AutomatoDePilha:
    """Reconhecedor de delimitadores balanceados, dirigido por tabela de transição."""

    def __init__(self):
        self.transicoes = {}
        self.pilha = []
        self.configurar_transicoes()

    def configurar_transicoes(self):
        """δ(estado, símbolo_lido, topo_pilha) -> (novo_estado, [símbolos_a_empilhar]).

        Empilhar [topo, X] preserva o topo e coloca X acima (push de X);
        empilhar [] consome o topo (pop); empilhar [topo] mantém a pilha (peek).
        """
        estados_ativos = [
            'q_inicio', 'q_lendo_paren', 'q_lendo_colch', 'q_lendo_chave',
            'q_fechando_paren', 'q_fechando_colch', 'q_fechando_chave'
        ]
        
        simbolos_topo = ['$', '(', '[', '{'] 

        for estado in estados_ativos:
            for topo in simbolos_topo:
                self.transicoes[(estado, '(', topo)] = ('q_lendo_paren', [topo, '('])
                self.transicoes[(estado, '[', topo)] = ('q_lendo_colch', [topo, '['])
                self.transicoes[(estado, '{', topo)] = ('q_lendo_chave', [topo, '{'])

            self.transicoes[(estado, ')', '(')] = ('q_fechando_paren', [])
            self.transicoes[(estado, ']', '[')] = ('q_fechando_colch', [])
            self.transicoes[(estado, '}', '{')] = ('q_fechando_chave', [])

            self.transicoes[(estado, '#', '$')] = ('q_aceita', ['$'])

    def processar(self, string_entrada):
        """
        Executa o Autômato de Pilha e gera o rastreamento (trace) de execução.
        """
        self.pilha = ['$'] 
        estado_atual = 'q_inicio'
        
        entrada_completa = list(string_entrada) + ['#']
        passo = 0

        print(f"\n{'='*50}")
        print(f"Analisando Sintaxe de Escopos: '{string_entrada}'")
        print(f"{'='*50}")

        for simbolo_lido in entrada_completa:
            if estado_atual in ['q_aceita', 'q_rejeita']:
                break

            topo_pilha = self.pilha.pop()
            
            pilha_visual = "".join(self.pilha) + str(topo_pilha)
            print(f"[Passo {passo:02d}] Estado: {estado_atual:<16} | Lendo: '{simbolo_lido}' | Pilha antes: [{pilha_visual}]")

            chave_transicao = (estado_atual, simbolo_lido, topo_pilha)

            if chave_transicao in self.transicoes:
                proximo_estado, simbolos_empilhar = self.transicoes[chave_transicao]

                for s in simbolos_empilhar:
                    self.pilha.append(s)

                estado_atual = proximo_estado
            else:
                print(f" -> ERRO DE SINTAXE: Nenhuma regra para estado '{estado_atual}' lendo '{simbolo_lido}' com topo '{topo_pilha}'.")
                estado_atual = 'q_rejeita'
                self.pilha.append(topo_pilha) 
                break

            passo += 1

        pilha_visual = "".join(self.pilha)
        print(f"\n[Resultado Final] Estado: {estado_atual} | Pilha Restante: [{pilha_visual}]")
        
        if estado_atual == 'q_aceita':
            print(">>> RESULTADO: CADEIA ACEITA <<<\n")
            return True
        else:
            print(">>> RESULTADO: CADEIA REJEITADA <<<\n")
            return False

if __name__ == "__main__":
    ap = AutomatoDePilha()
    
    while True:
        print("\n" + "="*45)
        print("MENU - AUTÔMATO DE PILHA ( (), [], {} )")
        print("="*45)
        print("1 - Inserir string manualmente")
        print("2 - Rodar exemplos predefinidos")
        print("3 - Encerrar programa")
        print("="*45)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            entrada = input("\nDigite a string de escopos (Ex: {[()]} ): ")
            ap.processar(entrada)
            
        elif opcao == '2':
            print("\n--- Teste 1: Caso Aceito (Aninhamento Perfeito) ---")
            ap.processar("{[()]}")
            
            print("\n--- Teste 2: Caso Rejeitado (Fechamento Incompatível) ---")
            ap.processar("{(})")
            
            print("\n--- Teste 3: Caso Rejeitado (Falta fechar um escopo) ---")
            ap.processar("([]")
            
            print("\n--- Teste 4: Caso Aceito (Escopos Sequenciais) ---")
            ap.processar("()[]{}")
            
        elif opcao == '3':
            print("\nEncerrando o programa...")
            break
            
        else:
            print("\nComando inválido. Por favor, digite 1, 2 ou 3.")