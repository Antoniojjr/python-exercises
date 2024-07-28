vetor_1 = []

for _ in range(10):
    nome = input('Digite os elementos:')
    vetor_1.append(nome)

nome_verifica = input() 

if nome_verifica in vetor_1:
    print('ACHEI')
else:
    print('NAÕ ACHEI')
        