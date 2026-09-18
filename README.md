# Trabalho P1 — Complexidade de Algoritmos
## Parte 1: demonstração prática de **O(n²)**

| | |
|---|---|
| **Aluno** | Luis Fillipe Damasceno Ramalho |
| **Matrícula** | 202321214 |
| **Disciplina** | Complexidade de Algoritmos |
| **Professor** | Msc. Antônio Tadeu Berardinelli Filho |
| **Big O escolhido** | `O(n²)` |

---

## O que é O(n²)

É a **complexidade quadrática**. Acontece quando o algoritmo usa **dois laços de
repetição aninhados** sobre os mesmos dados.

Na aula, a analogia foi: *"cada pessoa precisa conversar com todas as outras"* —
uma rodada de **todo mundo contra todo mundo**.

O resultado é que o trabalho **não cresce junto com os dados, cresce muito mais
rápido que eles**.

---

## O problema resolvido aqui

Encontrar nomes repetidos em uma lista, comparando cada nome com todos os outros.

```python
def encontrar_repetidos(nomes, mostrar=False):
    repetidos = []
    comparacoes = 0

    for i in range(len(nomes)):
        for j in range(i + 1, len(nomes)):
            comparacoes += 1

            if nomes[i] == nomes[j]:
                repetidos.append(nomes[i])

    return repetidos, comparacoes
```

O laço de fora roda `n` vezes e, para cada volta dele, o laço de dentro roda até
`n` vezes. Total: `n × n` → **O(n²)**.

O número exato de comparações é `n × (n − 1) / 2`, que é aproximadamente `n²/2`.
Como o Big O **ignora constantes**, a classificação continua sendo O(n²).

---

## A prova: quando n dobra, o trabalho fica 4× maior

Essa é a assinatura do O(n²), porque `(2n)² = 4n²`. O programa mede isso na
própria máquina:

```
     n    comparacoes    tempo (s)    cresceu
---------------------------------------------
   100          4.950       0.0003          -
   200         19.900       0.0012       4.0x
   400         79.800       0.0049       4.0x
   800        319.600       0.0214       4.0x
  1600      1.279.200       0.0788       4.0x
  3200      5.118.400       0.3711       4.0x
```

A coluna `cresceu` deu **exatamente 4,0x** em todas as linhas.
*(Os tempos variam de computador para computador; a coluna de comparações não.)*

E a conta para 1 milhão de nomes: **499.999.500.000 comparações**. Por isso um
algoritmo O(n²) funciona bem com pouco dado e trava com muito dado.

---

## Como executar

Precisa apenas de **Python 3**, sem bibliotecas externas.

```bash
python main.py
```

O programa roda sozinho e mostra:
1. Uma turma de 5 nomes, com cada comparação aparecendo na tela;
2. A tabela de crescimento medida na máquina.

---

## Resumo

| | |
|---|---|
| Nome | Complexidade quadrática |
| Como reconhecer | Dois laços de repetição aninhados |
| Se `n` dobra | O trabalho fica **~4× maior** |
| Exemplos reais | Comparar todos com todos, *bubble sort*, checar conflitos de horário |

> *"Complexidade = medir o esforço do algoritmo. Big O = representar como esse
> esforço cresce."* — Aula 01
