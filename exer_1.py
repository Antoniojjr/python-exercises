"""
1. Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor. Ao
final imprima o vetor armazenado nos dois sentidos.
"""

vetor = []

for _ in range(10):
    number = int(input('Digite um número:'))
    vetor.append(number)

print(vetor)
print(vetor[::-1])
