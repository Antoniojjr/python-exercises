n = int(input())
numero = 1

for i in range(1, n + 1):
    for j in range(1, i +1):
        print(numero, end=' ')
        numero += 1
    print()
    

