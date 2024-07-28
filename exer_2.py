
vetor_1 = []
vetor_2 = []

for _ in range(10):
    elementos = int(input('Digite os elementos:'))
    vetor_1.append(elementos)

for numero in vetor_1[::-1]:
    vetor_2.append(numero)

print(vetor_1)
print(vetor_2)
