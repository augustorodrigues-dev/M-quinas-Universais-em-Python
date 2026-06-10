# Declaração de Uso de Inteligência Artificial

**Disciplina:** Teoria da Computabilidade — CESUPA — 01/2026
**Turma:** CC5MA
**Equipe:** Augusto Pereira Rodrigues · César Ribeiro · Cauê Jadão

Esta declaração atende à Seção 8 da lauda da AV2. O uso de IA neste trabalho foi
**exclusivamente de apoio**: não substituiu o estudo, a modelagem formal, a
implementação ou a análise conceitual, que foram conduzidos e revisados pela
equipe.

## 1. Ferramentas utilizadas e datas aproximadas

| Ferramenta | Período aproximado | Finalidade |
|------------|--------------------|------------|
| Assistente de IA generativa (LLM) | Maio–Junho/2026 | Apoio à documentação, revisão e ferramental |

## 2. Finalidade do uso

A IA foi utilizada como ferramenta de apoio nas seguintes frentes:

- **Geração inicial e refino dos notebooks de visualização** (`*.ipynb`):
  estilização HTML/CSS do painel passo a passo (fila e pilha), a partir da
  lógica de transição já definida pela equipe.
- **Revisão textual e organização da documentação** (README, este arquivo e o
  relatório de rastreamento): estrutura, clareza e formatação Markdown.
- **Apoio à escrita dos testes automatizados** (`testes/`): sugestão de casos de
  borda adicionais (cadeia vazia, símbolos fora do alfabeto, fora de ordem).
- **Depuração**: conferência de consistência entre o código, as tabelas de
  transição apresentadas no README e as saídas dos rastreamentos.

## 3. Resumo dos prompts e dos trechos aproveitados

Os prompts giraram em torno de temas como:

- "Como exibir, em um notebook Jupyter, uma fila/pilha animada passo a passo com
  destaque do símbolo lido e do próximo estado?"
- "Revise a redação e a formatação Markdown deste README mantendo o conteúdo
  técnico."
- "Sugira casos de teste de fronteira para um reconhecedor de `aⁿbⁿcⁿ` e de
  parênteses balanceados."

**Trechos aproveitados:** principalmente o *layout* visual dos notebooks e a
organização/redação dos documentos. As sugestões de casos de teste foram
avaliadas e incorporadas quando pertinentes.

## 4. O que foi modificado, corrigido ou rejeitado pela equipe

- **Modelagem formal própria:** os estados, o alfabeto, as **tabelas de
  transição** e o algoritmo de reconhecimento das duas máquinas foram definidos
  pela equipe — não foram gerados por IA.
- **Correções aplicadas:** ajuste de rótulos/textos da interface dos notebooks
  (ex.: "ESTRUTURA DA FILA"), padronização de caminhos e instruções do README e
  remoção de código não utilizado.
- **Rejeições:** descartamos sugestões que "resolveriam" o problema chamando
  funções prontas da linguagem (o que violaria a Seção 6 da lauda) e mantivemos a
  simulação explícita do formalismo. Também revisamos cada saída para garantir
  que o relatório de rastreamento reflete a execução **real** do código.

## 5. Declaração da equipe

Declaramos que **todos os integrantes revisaram e compreendem** os trechos
incorporados ao trabalho — teoria, formalização, implementação e resultados — e
estão aptos a explicá-los e a justificá-los durante a arguição.
