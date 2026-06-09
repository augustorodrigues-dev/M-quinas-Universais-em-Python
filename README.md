# Trabalho AV2 - Teoria da Computabilidade 💻

## Informações Gerais

* **Instituição:** CESUPA - Centro Universitário do Estado do Pará
* **Disciplina:** Teoria da Computabilidade
* **Professor:** Daniel Leal Souza
* **Semestre:** 01/2026

## Equipe

* Augusto Pereira Rodrigues
* César Ribeiro
* Cauê Jadão

**Turma:** CC5MA

---

# 🎯 Objetivo do Trabalho

Este projeto consiste no desenvolvimento, simulação e análise comparativa de dois modelos clássicos da Teoria da Computabilidade, de acordo com as diretrizes formais da avaliação AV2.

Os modelos implementados foram:

1. **Máquina de Post (aⁿbⁿcⁿ)** — Demonstração de computabilidade em linguagens não regulares por meio de estruturas cíclicas de armazenamento em fila (FIFO).
2. **Autômato de Pilha (Validador Sintático)** — Reconhecimento de linguagens livres de contexto através do balanceamento e aninhamento de delimitadores utilizando pilha (LIFO).

O diferencial deste projeto está na disponibilização de simuladores visuais executados em **Jupyter Notebook**, permitindo acompanhar o comportamento da memória e das transições em tempo real.

---

# 💻 Modelos Implementados e Fundamentação Teórica

O núcleo de processamento das duas implementações foi desenvolvido utilizando o padrão **Table-Driven (Dirigido por Tabela)**.

Em vez de grandes estruturas condicionais (`if/else`), cada máquina consulta uma tabela de transições representada por dicionários Python, reproduzindo diretamente a função de transição formal:

δ(estado, símbolo) → próximo_estado

Dessa forma, o motor computacional permanece genérico e independente da linguagem reconhecida.


## 1. Máquina de Post

### Linguagem Reconhecida

**Linguagem:** L = { aⁿ bⁿ cⁿ | n ≥ 1 }

Classificação:

* Linguagem não regular
* Linguagem sensível ao contexto

### Estrutura de Armazenamento

* Fila (`collections.deque`)
* Política FIFO (*First In, First Out*)

### Controle Finito

* 10 estados formais

### Mecânica de Resolução

#### Fase 1 — Validação Estrutural

Os estados `q_val_a`, `q_val_a2`, `q_val_b` e `q_val_c` verificam:

* Existência de pelo menos um `a`, um `b` e um `c`
* Ordem correta dos símbolos
* Rejeição imediata de cadeias inválidas

#### Fase 2 — Cancelamento Cíclico

Após a validação estrutural:

1. Remove um símbolo `a`
2. Remove um símbolo `b`
3. Remove um símbolo `c`
4. Retorna ao início da fila

O ciclo é repetido até que reste apenas o marcador final `#`.

### Critério de Aceitação

A máquina aceita quando:

```text
#
```

for o único símbolo remanescente na fila.

---

## 2. Autômato de Pilha (PDA)

### Linguagem Reconhecida

**Linguagem:** L = { sequências bem formadas de (), [], {} }

Classificação:

* Linguagem Livre de Contexto (GLC)

### Estrutura de Armazenamento

* Pilha (`list`)
* Política LIFO (*Last In, First Out*)

### Controle Finito

* 9 estados

### Mecânica de Resolução

#### Empilhamento (Push)

Ao ler símbolos de abertura:

```text
(
[
{
```

o símbolo é armazenado no topo da pilha.

Formalmente:

`δ(q, a, X) → (p, [X, a])`

#### Desempilhamento (Pop)

Ao ler símbolos de fechamento:

```text
)
]
}
```

a máquina compara o símbolo lido com o topo da pilha.

Exemplo:

```text
[  -> ]
{  -> }
(  -> )
```

Se houver correspondência, o topo é removido.

Caso contrário, a execução é enviada para `q_rejeita`.

#### Critério de Aceitação

Ao final da leitura:

* A entrada deve ter sido totalmente consumida.
* A pilha deve conter apenas o marcador de fundo `$`.

---

# 📂 Estrutura do Repositório

```text
📦 trabalho-av2-computabilidade
│
├── implementacoes/
│   ├── maquina_post.py
│   ├── maquina_post.ipynb
│   ├── automato_pilha.py
│   └── automato_pilha.ipynb
│
│
├── testes/
│   ├── test_maquina_post.py
│   └── test_automato_pilha.py
│
├── slides/
│   └── apresentacao.pdf
│
├── .gitignore
├── uso_ia.md
└── README.md
```

---

# 🧪 Suíte de Testes Automatizados

Para garantir a confiabilidade das implementações, foram desenvolvidos testes automatizados utilizando a biblioteca nativa `unittest`.

## Executando Todos os Testes

```bash
python3 -m unittest discover -s testes
```

## Casos Cobertos

### Máquina de Post

Aceitação:

```text
abc
aabbcc
aaabbbccc
```

Rejeição:

```text
aabbc
aabbccc
abca
xyz
```

### Autômato de Pilha

Aceitação:

```text
{[()]}
()[]{}
```

Rejeição:

```text
{(}))
(([])
```

---

# 🚀 Instruções de Execução

## Pré-requisitos

* Python 3.10 ou superior

Nenhuma biblioteca externa é necessária.

---

## 1. Execução via Terminal

### Máquina de Post

```bash
python3 implementacoes/maquina_post.py
```

### Autômato de Pilha

```bash
python3 implementacoes/automato_pilha.py
```

---

## 2. Execução via Jupyter Notebook

Para a apresentação visual, execute:

```text
notebooks/simulador_visual.ipynb
```

O notebook exibe:

### Fita de Leitura

Destaca visualmente o símbolo atual sob processamento.

### Painel Preditivo

Exibe:

* Estado atual
* Próximo estado
* Símbolos válidos para transição

### Memória Visual

Representação gráfica de:

* Fila (FIFO) para a Máquina de Post
* Pilha (LIFO) para o PDA

---

# 🛠️ Uso de Inteligência Artificial

Ferramentas de IA generativa foram utilizadas exclusivamente como apoio em:

* Auxilio no desenvolvimento dos notebook;
* Auxilio nos testes;

Toda a modelagem formal, implementação dos algoritmos, construção dos diagramas e validação teórica foram realizadas pela equipe.

---

# 📚 Referências

HOPCROFT, John E.; MOTWANI, Rajeev; ULLMAN, Jeffrey D. *Introduction to Automata Theory, Languages and Computation*. 3. ed. Boston: Pearson, 2006.

SIPSER, Michael. *Introduction to the Theory of Computation*. 3. ed. Boston: Cengage Learning, 2012.

MENEZES, Paulo Blauth. *Linguagens Formais e Autômatos*. 6. ed. Porto Alegre: Sagra Luzzatto, 2011.

---

# 📄 Licença

Este repositório possui finalidade exclusivamente acadêmica, desenvolvido como componente avaliativo da disciplina **Teoria da Computabilidade** do curso de Ciência da Computação do **CESUPA (2026)**.
