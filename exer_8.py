
vetor_par = []
vetor_impar = []

for _ in range(10):
    
    number = int(input("Digite um número: "))

    if number % 2 == 0:
        vetor_par.append(number)
    elif number == 0:
        continue
    else:
        vetor_impar.append(number)

print(f'Soma nº par => {sum(vetor_par)}')
print(f'Soma nº ímpar => {sum(vetor_impar)}')
