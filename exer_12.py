
vetor_par = []
total_numeros = 0

while True:

    number = int(input("Digite um número: "))

    if number % 2 == 0 and number != 0:
        vetor_par.append(number)
        total_numeros += 1
    elif number == 0:
        print(sum(vetor_par) // total_numeros)
        break
    else:
        continue
