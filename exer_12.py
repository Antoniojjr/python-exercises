"""
12. Dado um conjunto de números inteiros informados pelo usuário, construa um programa
que calcule a média aritmética dos números pares. O valor de finalização será a entrada do
número 0 e não entrará nos cálculos. Observe que nada impede que o usuário forneça
quantos números ímpares quiser, com a ressalva de que eles não entrarão nos cálculos.
"""

vetor_par = []
total_numeros = 0

while True:

    number = int(input("Digite um número: "))

    if number % 2 == 0 and number != 0:
        vetor_par.append(number)
        total_numeros += 1
    elif number == 0:
        print(sum(vetor_par) // total_numeros)
        break
    else:
        continue
