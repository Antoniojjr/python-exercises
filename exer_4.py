"""
4. Ler um vetor com 10 nomes de pessoas, após pedir que o usuário digite um nome
qualquer de pessoa. Escrever a mensagem “ACHEI”, se o nome estiver armazenado no
vetor C ou “NÃO ACHEI” caso contrário.
"""

vetor_1 = []

for _ in range(10):
    nome = input('Digite os elementos:')
    vetor_1.append(nome)

nome_verifica = input() 

if nome_verifica in vetor_1:
    print('ACHEI')
else:
    print('NAÕ ACHEI')
        
