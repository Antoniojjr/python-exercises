
tamanho_vetor = int(input('Quantidade de elementos dos vetores: '))
vetor_1 = []
vetor_2 = []
lista_verifica = []

for _ in range(tamanho_vetor):
    ele_vetor_1 = input('Elementos do vetor 1: ')
    vetor_1.append(ele_vetor_1)

for _ in range(tamanho_vetor):
    ele_vetor_2 = input('Elementos do vetor 2: ')
    vetor_2.append(ele_vetor_2)

for elemento_1, elemento_2 in zip(vetor_1, vetor_2):
    if elemento_1 == elemento_2:
        lista_verifica.append(elemento_1)
    else:
        continue
    
if lista_verifica == vetor_1 == vetor_2:
    print('Mesmo conteúdo')
else:
    print('Conteúdo diferente')