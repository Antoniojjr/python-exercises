"""
3. Ler um vetor de 10 elementos inteiros e positivos. Criar um segundo vetor da seguinte
forma: os elementos de índice par receberão os respectivos elementos divididos por 2; os
elementos de índice ímpar receberão os respectivos elementos multiplicados por 3. Imprima
os dois vetores.
"""

vetor_1 = []
vetor_2 = []

for _ in range(10):
    x = int(input('Digite os elementos:'))
    vetor_1.append(x)

indice = 0
           
for numero in vetor_1:

    if indice % 2 == 0:
        vetor_2.append(numero/2)
    else:
        vetor_2.append(numero*3)
    indice += 1

print(vetor_1)
print(vetor_2)

