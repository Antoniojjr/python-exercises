"""
13. Uma loja utiliza o código “V” para transação à vista e “P” para transação à prazo. Faça
um programa que receba o código e o valor das transações. Quando o código for diferente
de “V” ou “P”, calcule e mostre:

a. O valor das compras à vista;
b. O valor das compras a prazo;
c. O valor total das compras efetuadas.
"""

a_vista = []
a_prazo = []

while True:

    codigo = input("Codigo da compra: ").upper()
    
    match codigo:

        case 'V':
            valor_compra = float(input('Valor da compra: '))
            a_vista.append(valor_compra)
        case 'P':
            valor_compra = float(input('Valor da compra: '))
            a_prazo.append(valor_compra)
        case __:
            print(f'Valor compras a vista: R$ {sum(a_vista)}')
            print(f'Valor compras a prazo: R$ {sum(a_prazo)}')
            print(f'Valor total das compras: R$ {sum(a_vista) + sum(a_prazo)}')
            break

