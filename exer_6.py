"""
6. Utilizando vetores, crie um programa que organize uma quantidade qualquer de números
inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem
crescente e depois os números ímpares em ordem decrescente.
"""

total_numeros = int(input())

vetor_par = []
vetor_impar = []

for _ in range(total_numeros):

    par_impar = int(input())

    if par_impar % 2 == 0 and par_impar != 0:
        vetor_par.append(par_impar)
    elif par_impar == 0:
        continue
    else:
        vetor_impar.append(par_impar)

vetor_par.sort()
vetor_impar.sort()
print(vetor_par + vetor_impar[::-1])
