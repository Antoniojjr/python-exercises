"""
9. Faça um programa que leia um número inteiro positivo n e imprima n linhas na tela com o
seguinte formato (exemplo se n = 4):
1
1 2
1 2 3
1 2 3 4
"""

linha = int(input("Número de linhas: "))


for n in range(1, linha + 1):
    for numero in range(1, n + 1):
        print(numero, end=' ')
    print()
    
    
