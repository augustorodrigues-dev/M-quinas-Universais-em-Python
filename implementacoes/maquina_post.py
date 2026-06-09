import time
from collections import deque

class MaquinaDePost:
    """
    Implementação formal da Máquina de Post para a linguagem a^n b^n c^n.
    Garante o cumprimento dos requisitos de complexidade da AV2 (>8 estados).
    """
    def __init__(self):
        self.transicoes = {}
        self.fila = deque()
        self.configurar_transicoes()

    def configurar_transicoes(self):
        self.transicoes[('q_val_a', 'a')] = ('q_val_a2', ['a'])
        self.transicoes[('q_val_a2', 'a')] = ('q_val_a2', ['a'])
        self.transicoes[('q_val_a2', 'b')] = ('q_val_b', ['b'])
        
        self.transicoes[('q_val_b', 'b')] = ('q_val_b', ['b'])
        self.transicoes[('q_val_b', 'c')] = ('q_val_c', ['c'])
        
        self.transicoes[('q_val_c', 'c')] = ('q_val_c', ['c'])
        self.transicoes[('q_val_c', '#')] = ('q_cancel_start', ['#'])

        self.transicoes[('q_cancel_start', 'a')] = ('q_skip_a', [])
        self.transicoes[('q_cancel_start', '#')] = ('q_aceita', [])

        self.transicoes[('q_skip_a', 'a')] = ('q_skip_a', ['a'])
        self.transicoes[('q_skip_a', 'b')] = ('q_skip_b', [])

        self.transicoes[('q_skip_b', 'b')] = ('q_skip_b', ['b'])
        self.transicoes[('q_skip_b', 'c')] = ('q_skip_c', [])

        self.transicoes[('q_skip_c', 'c')] = ('q_skip_c', ['c'])
        self.transicoes[('q_skip_c', '#')] = ('q_cancel_start', ['#'])

    def processar(self, string_entrada):
        self.fila = deque(list(string_entrada) + ['#'])
        estado_atual = 'q_val_a'
        passo = 0

        print(f"\n{'='*40}")
        print(f"Iniciando processamento: '{string_entrada}'")
        print(f"{'='*40}")

        while estado_atual not in ['q_aceita', 'q_rejeita']:
            conteudo_fila = "".join(self.fila)
            print(f"[Passo {passo:02d}] Estado: {estado_atual:<15} | Fila: {conteudo_fila}")
            
            if not self.fila:
                estado_atual = 'q_rejeita'
                break

            simbolo_lido = self.fila.popleft()

            chave = (estado_atual, simbolo_lido)
            if chave in self.transicoes:
                proximo_estado, simbolos_escrever = self.transicoes[chave]
                
                for s in simbolos_escrever:
                    self.fila.append(s)
                
                estado_atual = proximo_estado
            else:
                print(f" -> Nenhuma transição para ({estado_atual}, '{simbolo_lido}'). Rejeitando.")
                estado_atual = 'q_rejeita'
            
            passo += 1

        conteudo_fila = "".join(self.fila)
        print(f"[Passo {passo:02d}] Estado: {estado_atual:<15} | Fila: {conteudo_fila}")
        
        if estado_atual == 'q_aceita':
            print("\n>>> RESULTADO: CADEIA ACEITA <<<\n")
            return True
        else:
            print("\n>>> RESULTADO: CADEIA REJEITADA <<<\n")
            return False

if __name__ == "__main__":
    mp = MaquinaDePost()
    
    while True:
        print("\n" + "="*40)
        print("MENU - MÁQUINA DE POST (a^n b^n c^n)")
        print("="*40)
        print("1 - Inserir string manualmente")
        print("2 - Rodar exemplos predefinidos")
        print("3 - Encerrar programa")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            entrada = input("\nDigite a string para testar (Ex: aabbcc): ")
            mp.processar(entrada)
            
        elif opcao == '2':
            print("\n--- Executando Caso Aceito (Ideal) ---")
            mp.processar("aabbcc")
            
            print("\n--- Executando Caso Rejeitado (Faltando correspondência) ---")
            mp.processar("aabbc")
            
            print("\n--- Executando Caso Rejeitado (Fora de ordem) ---")
            mp.processar("abca")
            
        elif opcao == '3':
            print("\nEncerrando o programa...")
            break
        else:
            print("\nComando inválido. Por favor, digite 1, 2 ou 3.")