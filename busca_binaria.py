"""
Trabalho P1 - Complexidade de Algoritmos
Parte 2: demonstracao de apoio da apresentacao sobre O(log n)

Aluno: Luis Fillipe Damasceno Ramalho
Matricula: 202321214

A entrega da Parte 2 no AVA e o arquivo .pptx.
Este programa e opcional, so para rodar ao vivo se sobrar tempo.
"""

import math


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def mostrar_passos(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    passo = 0

    while inicio <= fim:
        passo += 1
        meio = (inicio + fim) // 2
        restantes = fim - inicio + 1

        print(f"    Passo {passo}: sobraram {restantes} numeros,"
              f" o meio e {lista[meio]}")

        if lista[meio] == alvo:
            print(f"             {lista[meio]} = {alvo}  ->  encontrado\n")
            return passo
        elif lista[meio] < alvo:
            print(f"             {alvo} > {lista[meio]}"
                  f"  ->  descarta a esquerda")
            inicio = meio + 1
        else:
            print(f"             {alvo} < {lista[meio]}"
                  f"  ->  descarta a direita")
            fim = meio - 1

    print(f"    {alvo} nao esta na lista\n")
    return passo


def main():
    print("=" * 58)
    print(" O(log n) - COMPLEXIDADE LOGARITMICA")
    print(" Luis Fillipe Damasceno Ramalho - 202321214")
    print("=" * 58)
    print("\n A cada passo, metade do problema e descartada.")
    print(" A busca binaria so funciona em lista ORDENADA.")

    lista = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 78, 85, 91, 96, 99]
    alvo = 23

    print(f"\n[1] Procurando o {alvo} em {len(lista)} numeros\n")
    print(f"    {lista}\n")
    passos = mostrar_passos(lista, alvo)

    print(f"    Busca binaria O(log n): {passos} passos")
    print(f"    Busca linear   O(n)   : {lista.index(alvo) + 1} passos")

    print("\n[2] Quantos passos o O(log n) precisa\n")
    print(f"    {'n':>15} {'O(n)':>16} {'O(log n)':>10}")
    print("    " + "-" * 43)

    for n in [10, 1_000, 1_000_000, 1_000_000_000]:
        texto_n = f"{n:,}".replace(",", ".")
        print(f"    {texto_n:>15} {texto_n:>16}"
              f" {math.ceil(math.log2(n)):>10}")

    print("\n    Cada vez que n dobra, e so 1 passo a mais.")
    print("\n" + "=" * 58 + "\n")


if __name__ == "__main__":
    main()
