# Relatório de Rastreamento de Execução

Documento gerado automaticamente por `rastreamento/gerar_rastreamento.py`. Cada trace abaixo é a saída literal do motor de simulação da respectiva máquina (mesma lógica dos arquivos em `implementacoes/`).

## 1. Máquina de Post — L = { aⁿbⁿcⁿ | n ≥ 1 }

A máquina opera sobre uma fila (FIFO). Cada passo mostra o estado de controle e o conteúdo atual da fila. O símbolo `#` é o marcador de fundo.

### Tabela-resumo dos testes

| # | Entrada | Categoria | Esperado | Obtido | Status |
|---|---------|-----------|----------|--------|--------|
| 1 | `abc` | aceito (n=1) | ACEITA | ACEITA | ✅ OK |
| 2 | `aabbcc` | aceito (n=2) | ACEITA | ACEITA | ✅ OK |
| 3 | `aaabbbccc` | aceito (n=3) | ACEITA | ACEITA | ✅ OK |
| 4 | `aabbc` | rejeitado (contagem desigual) | REJEITA | REJEITA | ✅ OK |
| 5 | `aaabbbcc` | rejeitado (falta um c) | REJEITA | REJEITA | ✅ OK |
| 6 | `abca` | rejeitado (fora de ordem) | REJEITA | REJEITA | ✅ OK |
| 7 | ε (vazia) | fronteira (cadeia vazia) | REJEITA | REJEITA | ✅ OK |
| 8 | `xyz` | inválido (fora do alfabeto) | REJEITA | REJEITA | ✅ OK |

### Traces detalhados (casos representativos)

**Entrada `aabbcc`**

```text
========================================
Iniciando processamento: 'aabbcc'
========================================
[Passo 00] Estado: q_val_a         | Fila: aabbcc#
[Passo 01] Estado: q_val_a2        | Fila: abbcc#a
[Passo 02] Estado: q_val_a2        | Fila: bbcc#aa
[Passo 03] Estado: q_val_b         | Fila: bcc#aab
[Passo 04] Estado: q_val_b         | Fila: cc#aabb
[Passo 05] Estado: q_val_c         | Fila: c#aabbc
[Passo 06] Estado: q_val_c         | Fila: #aabbcc
[Passo 07] Estado: q_cancel_start  | Fila: aabbcc#
[Passo 08] Estado: q_skip_a        | Fila: abbcc#
[Passo 09] Estado: q_skip_a        | Fila: bbcc#a
[Passo 10] Estado: q_skip_b        | Fila: bcc#a
[Passo 11] Estado: q_skip_b        | Fila: cc#ab
[Passo 12] Estado: q_skip_c        | Fila: c#ab
[Passo 13] Estado: q_skip_c        | Fila: #abc
[Passo 14] Estado: q_cancel_start  | Fila: abc#
[Passo 15] Estado: q_skip_a        | Fila: bc#
[Passo 16] Estado: q_skip_b        | Fila: c#
[Passo 17] Estado: q_skip_c        | Fila: #
[Passo 18] Estado: q_cancel_start  | Fila: #
[Passo 19] Estado: q_aceita        | Fila: 

>>> RESULTADO: CADEIA ACEITA <<<
```

**Entrada `aabbc`**

```text
========================================
Iniciando processamento: 'aabbc'
========================================
[Passo 00] Estado: q_val_a         | Fila: aabbc#
[Passo 01] Estado: q_val_a2        | Fila: abbc#a
[Passo 02] Estado: q_val_a2        | Fila: bbc#aa
[Passo 03] Estado: q_val_b         | Fila: bc#aab
[Passo 04] Estado: q_val_b         | Fila: c#aabb
[Passo 05] Estado: q_val_c         | Fila: #aabbc
[Passo 06] Estado: q_cancel_start  | Fila: aabbc#
[Passo 07] Estado: q_skip_a        | Fila: abbc#
[Passo 08] Estado: q_skip_a        | Fila: bbc#a
[Passo 09] Estado: q_skip_b        | Fila: bc#a
[Passo 10] Estado: q_skip_b        | Fila: c#ab
[Passo 11] Estado: q_skip_c        | Fila: #ab
[Passo 12] Estado: q_cancel_start  | Fila: ab#
[Passo 13] Estado: q_skip_a        | Fila: b#
[Passo 14] Estado: q_skip_b        | Fila: #
 -> Nenhuma transição para (q_skip_b, '#'). Rejeitando.
[Passo 15] Estado: q_rejeita       | Fila: 

>>> RESULTADO: CADEIA REJEITADA <<<
```

**Entrada ε (vazia)**

```text
========================================
Iniciando processamento: ''
========================================
[Passo 00] Estado: q_val_a         | Fila: #
 -> Nenhuma transição para (q_val_a, '#'). Rejeitando.
[Passo 01] Estado: q_rejeita       | Fila: 

>>> RESULTADO: CADEIA REJEITADA <<<
```

## 2. Autômato de Pilha — delimitadores balanceados (), [], {}

O autômato opera sobre uma pilha (LIFO). Cada passo mostra o estado de controle, o símbolo lido e a pilha antes da transição. `$` é o fundo da pilha.

### Tabela-resumo dos testes

| # | Entrada | Categoria | Esperado | Obtido | Status |
|---|---------|-----------|----------|--------|--------|
| 1 | `()` | aceito (par simples) | ACEITA | ACEITA | ✅ OK |
| 2 | `{[()]}` | aceito (aninhamento) | ACEITA | ACEITA | ✅ OK |
| 3 | `()[]{}` | aceito (sequencial) | ACEITA | ACEITA | ✅ OK |
| 4 | `{[()[]{}()]}` | aceito (misto) | ACEITA | ACEITA | ✅ OK |
| 5 | `{(})` | rejeitado (entrelaçado) | REJEITA | REJEITA | ✅ OK |
| 6 | `([]` | rejeitado (escopo aberto) | REJEITA | REJEITA | ✅ OK |
| 7 | `)(` | rejeitado (fecha antes de abrir) | REJEITA | REJEITA | ✅ OK |
| 8 | ε (vazia) | fronteira (cadeia vazia) | ACEITA | ACEITA | ✅ OK |

### Traces detalhados (casos representativos)

**Entrada `{[()]}`**

```text
==================================================
Analisando Sintaxe de Escopos: '{[()]}'
==================================================
[Passo 00] Estado: q_inicio         | Lendo: '{' | Pilha antes: [$]
[Passo 01] Estado: q_lendo_chave    | Lendo: '[' | Pilha antes: [${]
[Passo 02] Estado: q_lendo_colch    | Lendo: '(' | Pilha antes: [${[]
[Passo 03] Estado: q_lendo_paren    | Lendo: ')' | Pilha antes: [${[(]
[Passo 04] Estado: q_fechando_paren | Lendo: ']' | Pilha antes: [${[]
[Passo 05] Estado: q_fechando_colch | Lendo: '}' | Pilha antes: [${]
[Passo 06] Estado: q_fechando_chave | Lendo: '#' | Pilha antes: [$]

[Resultado Final] Estado: q_aceita | Pilha Restante: [$]
>>> RESULTADO: CADEIA ACEITA <<<
```

**Entrada `{(})`**

```text
==================================================
Analisando Sintaxe de Escopos: '{(})'
==================================================
[Passo 00] Estado: q_inicio         | Lendo: '{' | Pilha antes: [$]
[Passo 01] Estado: q_lendo_chave    | Lendo: '(' | Pilha antes: [${]
[Passo 02] Estado: q_lendo_paren    | Lendo: '}' | Pilha antes: [${(]
 -> ERRO DE SINTAXE: Nenhuma regra para estado 'q_lendo_paren' lendo '}' com topo '('.

[Resultado Final] Estado: q_rejeita | Pilha Restante: [${(]
>>> RESULTADO: CADEIA REJEITADA <<<
```

**Entrada `([]`**

```text
==================================================
Analisando Sintaxe de Escopos: '([]'
==================================================
[Passo 00] Estado: q_inicio         | Lendo: '(' | Pilha antes: [$]
[Passo 01] Estado: q_lendo_paren    | Lendo: '[' | Pilha antes: [$(]
[Passo 02] Estado: q_lendo_colch    | Lendo: ']' | Pilha antes: [$([]
[Passo 03] Estado: q_fechando_colch | Lendo: '#' | Pilha antes: [$(]
 -> ERRO DE SINTAXE: Nenhuma regra para estado 'q_fechando_colch' lendo '#' com topo '('.

[Resultado Final] Estado: q_rejeita | Pilha Restante: [$(]
>>> RESULTADO: CADEIA REJEITADA <<<
```

