"""
Trabalho P1 - Complexidade de Algoritmos
Parte 1: demonstracao pratica de O(n^2)

Aluno: Luis Fillipe Damasceno Ramalho
Matricula: 202321214

Problema: encontrar nomes repetidos em uma lista comparando
cada nome com todos os outros.
"""

import random
import time

random.seed(42)


def formatar(numero):
    return f"{numero:,}".replace(",", ".")


def encontrar_repetidos(nomes, mostrar=False):
    repetidos = []
    comparacoes = 0

    for i in range(len(nomes)):
        for j in range(i + 1, len(nomes)):
            comparacoes += 1

            if mostrar:
                print(f"    {comparacoes:>2}. {nomes[i]:<7} x {nomes[j]:<7}",
                      end="")

            if nomes[i] == nomes[j]:
                repetidos.append(nomes[i])
                if mostrar:
                    print("   <== repetido")
            elif mostrar:
                print()

    return repetidos, comparacoes


def gerar_nomes(quantidade):
    return [f"Aluno{random.randint(1, quantidade * 3)}"
            for _ in range(quantidade)]


def demonstracao():
    print("\n[1] Turma pequena: vendo cada comparacao acontecer\n")

    turma = ["Ana", "Bruno", "Carla", "Bruno", "Diego"]
    print(f"    Lista: {turma}\n")

    repetidos, comparacoes = encontrar_repetidos(turma, mostrar=True)

    print(f"\n    {len(turma)} nomes geraram {comparacoes} comparacoes.")
    print(f"    Repetidos encontrados: {repetidos}")


def medir_crescimento():
    print("\n[2] O que acontece quando n dobra\n")
    print(f"    {'n':>6} {'comparacoes':>14} {'tempo (s)':>12} {'cresceu':>10}")
    print("    " + "-" * 45)

    anterior = 0
    for n in [100, 200, 400, 800, 1600, 3200]:
        nomes = gerar_nomes(n)

        inicio = time.perf_counter()
        _, comparacoes = encontrar_repetidos(nomes)
        tempo = time.perf_counter() - inicio

        cresceu = "-" if anterior == 0 else f"{comparacoes / anterior:.1f}x"
        print(f"    {n:>6} {formatar(comparacoes):>14} {tempo:>12.4f}"
              f" {cresceu:>10}")

        anterior = comparacoes

    print("\n    Cada vez que n dobra, as comparacoes ficam 4x maiores.")
    print("    E exatamente isso que O(n^2) significa: (2n)^2 = 4 * n^2")


def main():
    print("=" * 58)
    print(" O(n^2) - COMPLEXIDADE QUADRATICA")
    print(" Luis Fillipe Damasceno Ramalho - 202321214")
    print("=" * 58)
    print("\n Cada nome e comparado com todos os outros nomes.")
    print(" Sao dois lacos de repeticao aninhados, entao o numero")
    print(" de comparacoes cresce na ordem de n x n.")

    demonstracao()
    medir_crescimento()

    total = 1_000_000 * 999_999 // 2
    print("\n" + "=" * 58)
    print(f" Com 1.000.000 de nomes seriam {formatar(total)} comparacoes.")
    print(" O(n^2) funciona bem com pouco dado e trava com muito dado.")
    print("=" * 58 + "\n")


if __name__ == "__main__":
    main()
