# Trabalho AV2 — Teoria da Computabilidade 💻

Simulação, formalização e análise de **dois modelos de computação distintos**: a
**Máquina de Post** (autômato de fila) e o **Autômato de Pilha** (PDA). Cada
modelo resolve um problema computacional diferente e expõe explicitamente o seu
formalismo — nenhuma resposta é obtida por função pronta da linguagem.

## Informações gerais

| Campo | Valor |
|-------|-------|
| **Instituição** | CESUPA — Centro Universitário do Estado do Pará |
| **Disciplina** | Teoria da Computabilidade |
| **Professor** | Daniel Leal Souza |
| **Semestre** | 01/2026 |
| **Turma** | CC5MA |

## Equipe

- Augusto Pereira Rodrigues
- César Ribeiro
- Cauê Jadão

> Equipe de 3 integrantes → exigência de **exatamente 2 máquinas/modelos
> distintos** (Seção 4 da lauda), cada um resolvendo um **problema diferente**.

## Modelos e problemas escolhidos

| # | Modelo (opção da lauda) | Memória | Problema resolvido | Classe da linguagem |
|---|--------------------------|---------|--------------------|---------------------|
| 1 | **Máquina de Post** (opção 6) | Fila — FIFO | Reconhecer `L₁ = { aⁿbⁿcⁿ \| n ≥ 1 }` | Sensível ao contexto (não livre de contexto) |
| 2 | **Autômato de Pilha** (opção 9) | Pilha — LIFO | Reconhecer delimitadores balanceados e aninhados `()`, `[]`, `{}` | Livre de contexto (determinística) |

**Por que os dois problemas são genuinamente diferentes** (Seção 7 da lauda):
não é a mesma linguagem com símbolos trocados. `L₁ = aⁿbⁿcⁿ` é **sensível ao
contexto e comprovadamente não livre de contexto** (nenhum PDA a reconhece),
enquanto a linguagem de delimitadores balanceados é **livre de contexto**. Os
problemas diferem na classe da linguagem, na estrutura de memória (FIFO × LIFO),
no critério de aceitação e na construção formal. A escolha foi proposital: ela
evidencia, na prática, a **diferença de poder computacional** entre os dois
modelos (ver [tabela comparativa](#7-comparação-entre-os-modelos)).

---

## Sumário

1. [Estrutura do repositório](#1-estrutura-do-repositório)
2. [Como executar](#2-como-executar)
3. [Arquitetura comum: motor dirigido por tabela](#3-arquitetura-comum-motor-dirigido-por-tabela)
4. [Máquina de Post — `aⁿbⁿcⁿ`](#4-máquina-de-post--aⁿbⁿcⁿ)
5. [Autômato de Pilha — delimitadores balanceados](#5-autômato-de-pilha--delimitadores-balanceados)
6. [Rastreamento de execução e testes](#6-rastreamento-de-execução-e-testes)
7. [Comparação entre os modelos](#7-comparação-entre-os-modelos)
8. [Uso de Inteligência Artificial](#8-uso-de-inteligência-artificial)
9. [Referências](#9-referências)

---

## 1. Estrutura do repositório

```text
M-quinas-Universais-em-Python/
├── implementacoes/
│   ├── maquina_post.py          # Máquina de Post (CLI + motor formal)
│   ├── maquina_post.ipynb        # simulador visual passo a passo (fila)
│   ├── automato_pilha.py         # Autômato de Pilha (CLI + motor formal)
│   └── automato_pilha.ipynb      # simulador visual passo a passo (pilha)
├── testes/
│   ├── test_maquina_post.py      # testes unitários (unittest)
│   └── test_automato_pilha.py
├── rastreamento/
│   ├── relatorio_rastreamento.md # tabelas de teste + traces reais
│   └── gerar_rastreamento.py     # script que reproduz o relatório
├── slides/
│   ├── apresentacao.pdf          # slides do seminário (PDF)
│   └── apresentacao.md           # fonte dos slides (Marp)
├── requirements.txt              # dependências (apenas para os notebooks)
├── uso_ia.md                     # declaração de uso de IA
├── .gitignore
└── README.md
```

## 2. Como executar

**Pré-requisito:** Python 3.10+ (testado em 3.14). Os simuladores em linha de
comando e os testes **não exigem nenhuma biblioteca externa**.

> Nos comandos abaixo, use `python` no Windows e `python3` no Linux/macOS.

### 2.1 Simuladores em terminal (menu interativo)

```bash
python implementacoes/maquina_post.py
python implementacoes/automato_pilha.py
```

Cada programa abre um menu com: (1) inserir uma cadeia manualmente, (2) rodar
exemplos predefinidos e (3) sair. Para cada cadeia, é impresso o **trace passo a
passo** (estado, memória e transição) e o veredito final.

### 2.2 Suíte de testes automatizados

```bash
python -m unittest discover -s testes -v
```

### 2.3 Relatório de rastreamento (reprodutível)

```bash
python rastreamento/gerar_rastreamento.py > rastreamento/relatorio_rastreamento.md
```

### 2.4 Simuladores visuais (Jupyter)

Os notebooks exibem a **fita de leitura**, a **memória** (fila ou pilha) e um
**painel preditivo** com o próximo estado e os símbolos válidos, animados passo
a passo.

```bash
pip install -r requirements.txt
jupyter notebook implementacoes/maquina_post.ipynb
jupyter notebook implementacoes/automato_pilha.ipynb
```

> Os notebooks deste repositório já estão **executados e com as saídas salvas**,
> permitindo auditar os resultados sem precisar rodá-los novamente.

## 3. Arquitetura comum: motor dirigido por tabela

As duas máquinas usam o padrão **table-driven**: em vez de cadeias de `if/else`,
a função de transição é uma **tabela** (dicionário Python) consultada a cada
passo, reproduzindo diretamente a relação formal `δ`. O motor de simulação fica
genérico e independente da linguagem; trocar a linguagem é trocar a tabela.

```python
# Máquina de Post:  δ(estado, símbolo_lido)            -> (próximo_estado, [escrever_no_fim])
# Autômato de Pilha: δ(estado, símbolo_lido, topo_pilha) -> (próximo_estado, [empilhar])
```

Isso atende à exigência da lauda (Seção 6) de **representar explicitamente o
formalismo** e **separar o modelo formal da rotina de simulação**.

---

## 4. Máquina de Post — `aⁿbⁿcⁿ`

### 4.1 Pesquisa conceitual

A **Máquina de Post**, originada nos trabalhos de **Emil Leon Post** (1936),
formaliza a computação por meio de **regras de produção** sobre cadeias. A
variante adotada aqui é o **autômato de fila** (*queue automaton*): um controle
finito acoplado a uma **fila** com disciplina **FIFO** — lê-se sempre o símbolo
da **frente** e escreve-se sempre no **fim**. Post chegou, de forma independente
de Turing, a um modelo equivalente: ambos capturam a mesma noção de
**procedimento efetivo**, reforçando a **Hipótese de Church-Turing**. O autômato
de fila é, de fato, **Turing-completo** — uma fila com leitura na frente e
escrita no fim permite simular a fita de uma Máquina de Turing.

Essa potência é exatamente o que torna `aⁿbⁿcⁿ` um bom exemplo: a linguagem é
**sensível ao contexto** e **não é livre de contexto** (consequência do Lema do
Bombeamento para LLCs), portanto **nenhum Autômato de Pilha a reconhece**. A
Máquina de Post reconhece-a sem dificuldade, ilustrando o salto de poder
computacional em relação ao PDA.

### 4.2 Formalização

Definimos `M = (Q, Σ, Γ, δ, q₀, #, F)`:

- **Q** (10 estados): `{ q_val_a, q_val_a2, q_val_b, q_val_c, q_cancel_start,`
  `q_skip_a, q_skip_b, q_skip_c, q_aceita, q_rejeita }` — **mais de 8 estados**,
  conforme Seção 7.
- **Σ** = `{ a, b, c }` (alfabeto de entrada).
- **Γ** = `{ a, b, c, # }` (alfabeto da fila); `#` é o **marcador de fundo**,
  inserido ao final da cadeia.
- **q₀** = `q_val_a` (estado inicial).
- **F** = `{ q_aceita }`; `q_rejeita` é alcançado quando não há transição
  definida (rejeição por bloqueio).
- **δ : Q × Γ → Q × Γ\*** — lê o símbolo da frente da fila e anexa ao fim a
  cadeia indicada. Anexar `[]` significa **apagar** o símbolo lido (consumo).

**Tabela de transição δ** (15 transições — acima do mínimo de 10 da Seção 7):

| Fase | Estado | Lê | → Estado | Escreve no fim |
|------|--------|----|----------|----------------|
| Validação | `q_val_a` | `a` | `q_val_a2` | `a` |
| Validação | `q_val_a2` | `a` | `q_val_a2` | `a` |
| Validação | `q_val_a2` | `b` | `q_val_b` | `b` |
| Validação | `q_val_b` | `b` | `q_val_b` | `b` |
| Validação | `q_val_b` | `c` | `q_val_c` | `c` |
| Validação | `q_val_c` | `c` | `q_val_c` | `c` |
| Validação | `q_val_c` | `#` | `q_cancel_start` | `#` |
| Cancelamento | `q_cancel_start` | `a` | `q_skip_a` | *(apaga)* |
| Cancelamento | `q_cancel_start` | `#` | **`q_aceita`** | — |
| Cancelamento | `q_skip_a` | `a` | `q_skip_a` | `a` |
| Cancelamento | `q_skip_a` | `b` | `q_skip_b` | *(apaga)* |
| Cancelamento | `q_skip_b` | `b` | `q_skip_b` | `b` |
| Cancelamento | `q_skip_b` | `c` | `q_skip_c` | *(apaga)* |
| Cancelamento | `q_skip_c` | `c` | `q_skip_c` | `c` |
| Cancelamento | `q_skip_c` | `#` | `q_cancel_start` | `#` |

**Critério de aceitação:** a máquina aceita quando, no início de um ciclo de
cancelamento (`q_cancel_start`), o único símbolo restante na fila é o marcador
`#` — ou seja, todos os `a`, `b` e `c` foram cancelados em igual quantidade.

### 4.3 Problema e mecânica de resolução

O problema é **decidir** se uma cadeia pertence a `L₁ = { aⁿbⁿcⁿ | n ≥ 1 }`. O
reconhecimento ocorre em duas fases:

1. **Validação estrutural** (`q_val_*`): garante a **forma** `a⁺b⁺c⁺` — pelo
   menos um de cada símbolo, na ordem correta. Cada símbolo lido é **reescrito**
   no fim, de modo que a cadeia volta intacta para a fila ao final da fase.
   Qualquer símbolo fora de ordem ou fora do alfabeto leva a `q_rejeita`.
2. **Cancelamento cíclico** (`q_cancel_start`, `q_skip_*`): a cada volta, a
   máquina **apaga exatamente um `a`, um `b` e um `c`** (rotacionando os demais
   pela fila) e devolve o `#` ao fim. O processo se repete até sobrar apenas o
   `#` (aceita) ou até faltar correspondência (rejeita).

Como a fase 1 já garante a forma `aⁱbʲcᵏ` com `i, j, k ≥ 1`, e a fase 2 só aceita
quando `i = j = k`, a linguagem reconhecida é **exatamente** `aⁿbⁿcⁿ`.

### 4.4 Análise técnica

- **Por que não é trivial:** o problema **não pode** ser resolvido por um
  autômato finito nem por um autômato de pilha. Exige comparar **três**
  contagens simultaneamente — algo que a disciplina FIFO resolve por
  cancelamento síncrono, usando a memória ilimitada da fila.
- **Terminação:** cada ciclo completo de cancelamento reduz o comprimento da
  fila em 3 símbolos (`aᵏbᵏcᵏ# → aᵏ⁻¹bᵏ⁻¹cᵏ⁻¹#`); logo a máquina **sempre para**,
  aceitando ou rejeitando (é um **decisor**, não apenas um reconhecedor).
- **Caso de fronteira:** a cadeia vazia `ε` é **rejeitada**, pois a definição
  exige `n ≥ 1` (ver [rastreamento](rastreamento/relatorio_rastreamento.md)).
- **Limitações:** o alfabeto é fixo (`a`, `b`, `c`); generalizar para `k` blocos
  exigiria estender estados e a tabela. A implementação prioriza clareza
  didática sobre otimização (a rotação pela fila é `O(n²)` no pior caso).

➡ Código: [`implementacoes/maquina_post.py`](implementacoes/maquina_post.py) ·
Visual: [`implementacoes/maquina_post.ipynb`](implementacoes/maquina_post.ipynb)

---

## 5. Autômato de Pilha — delimitadores balanceados

### 5.1 Pesquisa conceitual

O **Autômato de Pilha** (*Pushdown Automaton*, PDA) é o modelo canônico das
**linguagens livres de contexto** (LLCs): um **controle finito** acoplado a uma
**pilha** (disciplina **LIFO**). A pilha funciona como uma memória de
**aninhamento** — ideal para estruturas balanceadas, que aparecem em expressões
aritméticas, sintaxe de linguagens de programação e marcação (HTML/XML). É
**estritamente mais poderoso** que um autômato finito (que não reconhece nem
`aⁿbⁿ`) e **estritamente menos poderoso** que a Máquina de Turing/Post (não
reconhece `aⁿbⁿcⁿ`). O reconhecimento de parênteses balanceados é o exemplo
arquetípico de uso da pilha como contador aninhado.

### 5.2 Formalização

Definimos `P = (Q, Σ, Γ, δ, q₀, $, F)`:

- **Q** (9 estados): `{ q_inicio, q_lendo_paren, q_lendo_colch, q_lendo_chave,`
  `q_fechando_paren, q_fechando_colch, q_fechando_chave, q_aceita, q_rejeita }`
  — **mais de 8 estados**, conforme Seção 7.
- **Σ** = `{ (, ), [, ], {, } }` (alfabeto de entrada).
- **Γ** = `{ $, (, [, { }` — apenas **símbolos de abertura** são empilhados; `$`
  é o **fundo da pilha**.
- **q₀** = `q_inicio`; o fundo `$` inicia na pilha.
- **F** = `{ q_aceita }`.
- **δ : Q × (Σ ∪ {#}) × Γ → Q × Γ\*** — lê (símbolo, topo) e devolve a nova
  pilha. O símbolo `#` é o **fim de entrada**, gerado internamente.

**Esquema da função de transição** (gerada para todos os estados ativos):

| Ação | Lê | Topo | → Estado | Efeito na pilha |
|------|----|------|----------|-----------------|
| Abrir | `(` | qualquer | `q_lendo_paren` | empilha `(` |
| Abrir | `[` | qualquer | `q_lendo_colch` | empilha `[` |
| Abrir | `{` | qualquer | `q_lendo_chave` | empilha `{` |
| Fechar | `)` | `(` | `q_fechando_paren` | desempilha (*pop*) |
| Fechar | `]` | `[` | `q_fechando_colch` | desempilha (*pop*) |
| Fechar | `}` | `{` | `q_fechando_chave` | desempilha (*pop*) |
| Fim | `#` | `$` | **`q_aceita`** | mantém `$` |
| *(qualquer outra combinação)* | — | — | `q_rejeita` | — |

**Critério de aceitação:** a entrada é aceita se, ao ler o marcador de fim `#`, o
topo da pilha for o fundo `$` (toda abertura foi casada com seu fechamento
correspondente). Isso equivale à **aceitação por pilha vazia** combinada com
**estado final**.

> **Decisão de modelagem (defensável na arguição):** um reconhecedor mínimo de
> parênteses precisaria de **um único** estado de controle — a decisão é tomada
> pela pilha. Optamos por **enriquecer o controle finito** para que o estado
> registre o **tipo da última operação** (qual delimitador foi aberto/fechado).
> Isso não altera a linguagem reconhecida, mas torna o **rastreamento
> autoexplicativo** e demonstra didaticamente que **estado e pilha são
> componentes independentes** do modelo.

### 5.3 Problema e mecânica de resolução

O problema é **decidir** se uma cadeia é uma sequência **bem formada** dos três
tipos de delimitadores — exigindo **casamento por tipo** e **aninhamento
correto** (`{[()]}` é válido; `{(})` não é, pois `(` precisa fechar antes de
`{`). A cada abertura, empilha-se o delimitador; a cada fechamento, verifica-se
se o topo é a abertura **do mesmo tipo** e desempilha-se. Discrepância de tipo,
fechamento sem abertura, ou abertura sem fechamento levam à rejeição.

### 5.4 Análise técnica

- **Por que não é trivial:** o casamento de **três tipos** de delimitadores
  aninhados **não é regular** — um autômato finito não consegue lembrar a ordem
  arbitrária de aberturas. A pilha resolve isso naturalmente, em **um único
  passo de leitura** por símbolo (`O(n)`).
- **Caso de fronteira:** a cadeia vazia `ε` é **aceita**, pois a sequência vazia
  é (vacuosamente) balanceada — coerente com a gramática `S → SS | (S) | [S] |
  {S} | ε`.
- **Determinismo:** este PDA é **determinista** — há no máximo uma transição
  aplicável por configuração, o que torna o reconhecimento eficiente.
- **Limitações:** reconhece **estrutura**, não **semântica**; e, por ser livre
  de contexto, **não** consegue impor restrições sensíveis ao contexto como
  `aⁿbⁿcⁿ` (daí a escolha da Máquina de Post para o outro problema).

➡ Código: [`implementacoes/automato_pilha.py`](implementacoes/automato_pilha.py) ·
Visual: [`implementacoes/automato_pilha.ipynb`](implementacoes/automato_pilha.ipynb)

---

## 6. Rastreamento de execução e testes

O relatório completo, com **tabela de teste** (entrada, categoria, esperado,
obtido, status) e **traces passo a passo** para casos aceitos, rejeitados e de
fronteira, está em
**[`rastreamento/relatorio_rastreamento.md`](rastreamento/relatorio_rastreamento.md)**
e é **reproduzível** via `rastreamento/gerar_rastreamento.py`.

Resumo dos casos cobertos pelos testes automatizados (`unittest`):

| Máquina | Aceitos | Rejeitados / inválidos / fronteira |
|---------|---------|-------------------------------------|
| **Máquina de Post** | `abc`, `aabbcc`, `aaabbbccc` | `aabbc`, `abbcc`, `aabcc`, `aabbccc`, `abca`, `cbaf`, `bca`, `xyz`, `ε` |
| **Autômato de Pilha** | `{[()]}`, `()[]{}`, `{[()[]{}()]}`, `()` | `{(})`, `{[(])}`, `)(]`, `([]`, `{[()}`, `(` |

```bash
python -m unittest discover -s testes -v   # 7 testes, todos passando
```

## 7. Comparação entre os modelos

| Critério | Máquina de Post (fila) | Autômato de Pilha |
|----------|------------------------|-------------------|
| Estrutura de memória | Fila — **FIFO** | Pilha — **LIFO** |
| Acesso à memória | Lê na frente, escreve no fim | Lê/escreve só no topo |
| Linguagem do exemplo | `aⁿbⁿcⁿ` (**sensível ao contexto**) | balanceados (**livre de contexto**) |
| Classe de máquina | **Turing-completa** | Reconhecedor de LLC |
| Poder computacional | Equivalente à Máquina de Turing | Estritamente menor que MT |
| Reconhece `aⁿbⁿcⁿ`? | **Sim** | **Não** (Lema do Bombeamento p/ LLC) |
| Aceita cadeia vazia `ε`? | Não (`n ≥ 1`) | Sim (vacuosamente balanceada) |
| Critério de aceitação | Fila reduzida a `#` | Pilha reduzida a `$` ao fim |

Esta comparação é o fio condutor do seminário: os mesmos princípios
(controle finito + memória auxiliar) produzem **poderes computacionais
diferentes** conforme a **disciplina de acesso** à memória.

## 8. Uso de Inteligência Artificial

A declaração completa (ferramenta, datas, finalidade, prompts, o que foi
modificado/rejeitado e declaração de revisão pela equipe) está em
**[`uso_ia.md`](uso_ia.md)**.

Em resumo: ferramentas de IA generativa foram usadas **apenas como apoio** na
construção dos notebooks de visualização e na organização da documentação/testes.
**Toda a modelagem formal, a tabela de transições, a lógica de reconhecimento e a
análise teórica foram desenvolvidas e revisadas pela equipe**, que compreende
integralmente cada trecho e está apta a explicá-lo na arguição.

## 9. Referências

- DIVERIO, Tiarajú Asmuz; MENEZES, Paulo Blauth. **Teoria da Computação:
  Máquinas Universais e Computabilidade**. 3. ed. Porto Alegre: Bookman, 2011.
- MENEZES, Paulo Blauth. **Linguagens Formais e Autômatos**. 6. ed. Porto
  Alegre: Bookman, 2011.
- HOPCROFT, John E.; MOTWANI, Rajeev; ULLMAN, Jeffrey D. **Introduction to
  Automata Theory, Languages and Computation**. 3. ed. Boston: Pearson, 2006.
- SIPSER, Michael. **Introduction to the Theory of Computation**. 3. ed.
  Boston: Cengage Learning, 2013.
- POST, Emil L. *Finite Combinatory Processes — Formulation 1*. Journal of
  Symbolic Logic, v. 1, n. 3, p. 103–105, 1936.

---

> Repositório de finalidade **exclusivamente acadêmica**, desenvolvido como
> componente avaliativo (AV2) da disciplina **Teoria da Computabilidade** do
> curso de Ciência da Computação do **CESUPA — 01/2026**.
