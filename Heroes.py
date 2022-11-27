print("Responda SI o NO: ")
hero=input('Puede Volar?')
if hero == 'SI':
    human=input('Es humano?:')
    if human == 'SI':
        mask=input('Tienes mascara?: ')
        if mask == 'SI':
            print('Tu heroes es Iron Man')
        else:
            print('Tu heroe es Captain Marvel')
    else:
        mask=input('Tienes mascara?: ')
        if mask == 'SI':
            print('Tu heroes es Ronan Acuser')
        else:
            print('Tu heroe es Vision')               
else:
    human=input('Es humano?:')
    if human == 'SI':
        mask=input('Tienes mascara?: ')
        if mask == 'SI':
            print('Tu heroes es Spider Man')
        else:
            print('Tu heroe es Hulk')
    else:
        mask=input('Tienes mascara?: ')
        if mask == 'SI':
            print('Tu heroes es Black Bolt')
        else:
            print('Tu heroe es Thanos')     
        
    