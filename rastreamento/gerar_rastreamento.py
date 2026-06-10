# -*- coding: utf-8 -*-
"""Gera o relatório de rastreamento de execução das duas implementações.

Executa as máquinas sobre um conjunto fixo de entradas (casos aceitos,
rejeitados e de fronteira), captura o trace passo a passo produzido pelo
próprio motor de cada máquina e emite um relatório em Markdown com:

  * tabela-resumo (entrada, categoria, esperado, obtido, status);
  * traces detalhados de casos representativos.

Uso:
    python rastreamento/gerar_rastreamento.py > rastreamento/relatorio_rastreamento.md

O relatório versionado neste repositório foi produzido exatamente por este
script, garantindo reprodutibilidade (a lauda exige saída obtida coerente com
a apresentada).
"""
import io
import os
import sys
from contextlib import redirect_stdout

# Garante saída UTF-8 mesmo em consoles Windows (cp1252), para que símbolos
# como ⁿ, ε, →, ✅ sejam escritos corretamente no relatório.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "implementacoes"))
)

from automato_pilha import AutomatoDePilha  # noqa: E402
from maquina_post import MaquinaDePost  # noqa: E402


def executar(maquina_factory, entrada):
    """Roda uma máquina sobre `entrada` e devolve (resultado_bool, trace_str)."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        resultado = maquina_factory().processar(entrada)
    return resultado, buffer.getvalue().strip()


def render_repr(entrada):
    return "ε (vazia)" if entrada == "" else f"`{entrada}`"


def secao(titulo, descricao, factory, casos, detalhar):
    print(f"## {titulo}\n")
    print(descricao + "\n")

    print("### Tabela-resumo dos testes\n")
    print("| # | Entrada | Categoria | Esperado | Obtido | Status |")
    print("|---|---------|-----------|----------|--------|--------|")
    resultados = {}
    for i, (entrada, categoria, esperado) in enumerate(casos, start=1):
        obtido, trace = executar(factory, entrada)
        resultados[entrada] = (obtido, trace)
        rotulo_esp = "ACEITA" if esperado else "REJEITA"
        rotulo_obt = "ACEITA" if obtido else "REJEITA"
        status = "✅ OK" if obtido == esperado else "❌ FALHA"
        print(
            f"| {i} | {render_repr(entrada)} | {categoria} | {rotulo_esp} | "
            f"{rotulo_obt} | {status} |"
        )
    print()

    print("### Traces detalhados (casos representativos)\n")
    for entrada in detalhar:
        _, trace = resultados[entrada]
        print(f"**Entrada {render_repr(entrada)}**\n")
        print("```text")
        print(trace)
        print("```\n")


CASOS_POST = [
    ("abc", "aceito (n=1)", True),
    ("aabbcc", "aceito (n=2)", True),
    ("aaabbbccc", "aceito (n=3)", True),
    ("aabbc", "rejeitado (contagem desigual)", False),
    ("aaabbbcc", "rejeitado (falta um c)", False),
    ("abca", "rejeitado (fora de ordem)", False),
    ("", "fronteira (cadeia vazia)", False),
    ("xyz", "inválido (fora do alfabeto)", False),
]

CASOS_PILHA = [
    ("()", "aceito (par simples)", True),
    ("{[()]}", "aceito (aninhamento)", True),
    ("()[]{}", "aceito (sequencial)", True),
    ("{[()[]{}()]}", "aceito (misto)", True),
    ("{(})", "rejeitado (entrelaçado)", False),
    ("([]", "rejeitado (escopo aberto)", False),
    (")(", "rejeitado (fecha antes de abrir)", False),
    ("", "fronteira (cadeia vazia)", True),
]


def main():
    print("# Relatório de Rastreamento de Execução\n")
    print(
        "Documento gerado automaticamente por `rastreamento/gerar_rastreamento.py`. "
        "Cada trace abaixo é a saída literal do motor de simulação da respectiva "
        "máquina (mesma lógica dos arquivos em `implementacoes/`).\n"
    )

    secao(
        "1. Máquina de Post — L = { aⁿbⁿcⁿ | n ≥ 1 }",
        "A máquina opera sobre uma fila (FIFO). Cada passo mostra o estado de "
        "controle e o conteúdo atual da fila. O símbolo `#` é o marcador de fundo.",
        MaquinaDePost,
        CASOS_POST,
        detalhar=["aabbcc", "aabbc", ""],
    )

    secao(
        "2. Autômato de Pilha — delimitadores balanceados (), [], {}",
        "O autômato opera sobre uma pilha (LIFO). Cada passo mostra o estado de "
        "controle, o símbolo lido e a pilha antes da transição. `$` é o fundo da pilha.",
        AutomatoDePilha,
        CASOS_PILHA,
        detalhar=["{[()]}", "{(})", "([]"],
    )


if __name__ == "__main__":
    main()
