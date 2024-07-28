"""
11. Faça um programa que calcule N! (fatorial de N), sendo que o valor inteiro de N é
fornecido pelo usuário. Sabe-se que:

N! = 1 * 2 * 3 * 4 * ... * (N – 1) * N; Exemplo: fatorial de 4 é 1 * 2 * 3 * 4 = 24.
0! = 1, por definição.
"""

number = int(input('Digite um número: '))

fatorial = 1

for i in range(1, number +1):
    
    f = i * fatorial

    fatorial = f

print(fatorial)
