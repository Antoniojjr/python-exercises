
vetor = []
while True:

    opcoes = int(input('(1) Adicionar um número ao vetor.\n'
                        '(2) Remover um número do vetor.\n'
                        '(3) Exibir o vetor completo.\n'
                        '(4) Encontrar e exibir o maior e o menor número no vetor.\n'
                        '(5) Calcular e exibir a soma de todos os números no vetor.\n'
                        '(6) Sair.\n'))

    match opcoes:

        case 1:
            numero = float(input('Digite o número para adicionar: '))
            vetor.append(numero)
        case 2:    
            numero = float(input('Digite o número para remover: '))
            vetor.remove(numero)
        case 3:
            print(vetor)
        case 4:
            print(f'Maior nº => {max(vetor)}')
            print(f'Menor nº => {min(vetor)}')
            
        case 5:
            print(f'Soma dos nº => {sum(vetor)}')
        case 6:
            break
        case _:
            print('Comando inválido!')
            continue