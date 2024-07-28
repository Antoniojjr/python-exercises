
number = int(input('Digite um número: '))

fatorial = 1

for i in range(1, number +1):
    
    f = i * fatorial

    fatorial = f

print(fatorial)