
v_tinto = 0
v_branco = 0
v_rose = 0
total = 0

while True:

    tipo = input('Tipo do vinho: ').upper()

    match tipo:

        case 'T':
            v_tinto += 1
            total += 1
    
        case 'B':
            v_branco += 1
            total += 1
            
        case 'R':
            v_rose += 1
            total += 1
            
        case __:
            break

print(f'Porcetagem de vinho tinto: {v_tinto * (100/total):.2f} %')
print(f'Porcetagem de vinho branco: {v_branco * (100/total):.2f} %')
print(f'Porcetagem de vinho rose: {v_rose * (100/total):.2f} %')

            
            
