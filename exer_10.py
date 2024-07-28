"""
10. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
linhas do chamado triângulo de Floyd. O exemplo abaixo mostra o triângulo de Floyd com 4
linhas.
1
2 3
4 5 6
7 8 9 10
"""

n = int(input())
numero = 1

for i in range(1, n + 1):
    for j in range(1, i +1):
        print(numero, end=' ')
        numero += 1
    print()
    

