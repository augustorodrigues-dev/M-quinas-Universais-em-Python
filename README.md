# Trabalho AV2 - Teoria da Computabilidade 💻

## Informações Gerais

**Instituição:** CESUPA - Centro Universitário do Estado do Pará
**Disciplina:** Teoria da Computabilidade
**Professor:** Daniel Leal Souza
**Semestre:** 01/2026

---

## Equipe

**Turma:** CC5MA / CC5NA *(preencher conforme aplicável)*

* Augusto Pereira Rodrigues
* César Ribeiro
* Fernando Fonseca
* *(Nome do 4º integrante, se houver)*

---

# Objetivo do Trabalho

Este projeto tem como objetivo implementar e analisar dois modelos clássicos da Teoria da Computabilidade:

1. **Máquina de Post**
2. **Autômato de Pilha**

Além da implementação computacional, o trabalho contempla a documentação dos modelos, rastreamento das execuções e análise dos resultados obtidos.

---

# Modelos Implementados

## 1. Máquina de Post

### Problema Resolvido

Reconhecimento da linguagem:

[
L = {a^n b^n c^n \mid n \geq 1}
]

### Descrição

A implementação utiliza uma **Máquina de Post baseada em fila (FIFO – First In, First Out)**.

O algoritmo opera em duas etapas principais:

#### Fase 1 — Validação Estrutural

Verifica se a entrada segue o padrão:

```text
aⁿ bⁿ cⁿ
```

Garantindo:

* Pelo menos um símbolo `a`
* Pelo menos um símbolo `b`
* Pelo menos um símbolo `c`
* Ordem correta dos símbolos

#### Fase 2 — Cancelamento Cíclico

Após a validação estrutural, a máquina realiza ciclos sucessivos de cancelamento:

1. Remove um `a`
2. Remove um `b`
3. Remove um `c`
4. Retorna ao início da fila

O processo se repete até que todos os símbolos sejam consumidos.

### Características

* Modelo: Máquina de Post (Fila)
* Estrutura de dados: `deque`
* Total de estados: 10
* Estratégia: FIFO
* Linguagem reconhecida: não regular

### Exemplos

#### Cadeias Aceitas

```text
abc
aabbcc
aaabbbccc
aaaabbbbcccc
```

#### Cadeias Rejeitadas

```text
aabbc
abca
aabbbccc
abbccc
```

---

## 2. Autômato de Pilha

### Problema Resolvido

Validação de sequências corretamente balanceadas de delimitadores:

[
L = {\text{sequências bem formadas de } (), [], {}}
]

### Descrição

A implementação utiliza um **Autômato de Pilha (PDA)** para verificar o balanceamento e o aninhamento correto dos símbolos:

```text
()
[]
{}
```

A pilha é utilizada para armazenar símbolos de abertura e garantir que cada símbolo de fechamento corresponda ao último símbolo aberto.

### Exemplos

#### Cadeias Aceitas

```text
()
([])
{[()]}
```

#### Cadeias Rejeitadas

```text
(
([)]
{]
```

### Características

* Modelo: Autômato de Pilha
* Estrutura de dados: Pilha (LIFO)
* Estratégia: Push e Pop
* Linguagem reconhecida: livre de contexto

---

# Estrutura do Repositório

```text
📦 trabalho-av2-computabilidade
│
├── implementacoes
│   ├── maquina_post.py
│   └── automato_pilha.py
│
├── testes
│   ├── logs_post/
│   ├── logs_pilha/
│   └── capturas_execucao/
│
├── slides
│   └── apresentacao.pdf
│
├── uso_ia.md
│
└── README.md
```

### Descrição dos Diretórios

| Diretório        | Conteúdo                                     |
| ---------------- | -------------------------------------------- |
| `implementacoes` | Código-fonte dos modelos computacionais      |
| `testes`         | Logs, rastreamentos e evidências de execução |
| `slides`         | Apresentação utilizada na defesa do trabalho |
| `uso_ia.md`      | Declaração de uso de Inteligência Artificial |
| `README.md`      | Documentação principal do projeto            |

---

# Dependências

O projeto foi desenvolvido utilizando apenas recursos nativos da linguagem Python.

### Requisitos

* Python 3.10 ou superior

### Bibliotecas Utilizadas

```python
collections
time
```

Nenhuma instalação adicional é necessária.

---

# Execução

Abra um terminal na raiz do projeto e execute:

### Máquina de Post

```bash
python3 implementacoes/maquina_post.py
```

### Autômato de Pilha

```bash
python3 implementacoes/automato_pilha.py
```

---

# Casos de Teste

A implementação disponibiliza exemplos prontos para validação.

### Máquina de Post

Entrada:

```text
aabbcc
```

Resultado:

```text
ACEITA
```

Entrada:

```text
aabbc
```

Resultado:

```text
REJEITA
```

### Autômato de Pilha

Entrada:

```text
{[()]}
```

Resultado:

```text
ACEITA
```

Entrada:

```text
([)]
```

Resultado:

```text
REJEITA
```

---

# Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial foram utilizadas como apoio para:

* Estudo dos modelos computacionais;
* Revisão de código;
* Documentação;
* Organização da estrutura do projeto.

Toda modelagem, implementação, testes e validação foram realizados pela equipe.

---

# Referências

* HOPCROFT, John E.; MOTWANI, Rajeev; ULLMAN, Jeffrey D. *Introduction to Automata Theory, Languages and Computation*.
* SIPSER, Michael. *Introduction to the Theory of Computation*.
* MENEZES, Paulo Blauth. *Linguagens Formais e Autômatos*.

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de **Teoria da Computabilidade – CESUPA (2026)**.
