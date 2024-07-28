
vetor_1 = []
vetor_2 = []
vetor_diferenca = []
vetor_soma = []
vetor_multiplica = []

for _ in range(20):
    numero = int(input('Elementos lista 1: '))
    vetor_1.append(numero)

for _ in range(20):
    numero = int(input('Elementos lista 2: '))
    vetor_2.append(numero)

for number_1, number_2 in zip(vetor_1, vetor_2):

    vetor_diferenca.append(number_1 - number_2)
    vetor_soma.append(number_1 + number_2)
    vetor_multiplica.append(number_1 * number_2)


print(vetor_1)
print(vetor_2)
print(vetor_diferenca)
print(vetor_soma)
print(vetor_multiplica)


