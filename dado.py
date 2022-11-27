import random
def dado_magico():
    print('Bienvenido a batalla de dados')
    namePlayerOne=input('Ingrese su nombre Jugador 1: ')
    namePlayerTwo=input('Ingrese su nombre Jugador 2: ')
    n_rondas=int(input('Selecciona el numero de rondas (1-3): '))
    rondas=0
    points_one=0
    points_two=0
    while(n_rondas > rondas):
        rPlayOne=0
        rPlayTwo=0
        playGameOne=input(f'{namePlayerOne} Desea lanzar el dado?(Y/N): ')
        if(playGameOne.lower() == 'y'):
            rPlayOne=random.randint(1,6)
            print(f'El dado cayó en: {rPlayOne}')
        elif(playGameOne.lower() == 'n'):
            rPlayOne=1
        playGameTwo=input(f'{namePlayerTwo} Desea lanzar el dado?(Y/N): ')
        if(playGameTwo.lower() == 'y'):
            rPlayTwo=random.randint(1,6)
            print(f'El dado cayó en: {rPlayTwo}')
        elif(playGameTwo.lower() == 'n'):
            rPlayTwo=1
        if(rPlayOne>rPlayTwo):
            points_one += 1
            print(f'{namePlayerOne} Ganó esta ronda')
            rondas += 1
        elif(rPlayOne<rPlayTwo):
            points_two += 1
            print(f'{namePlayerTwo} Ganó esta ronda')
            rondas += 1
        elif(rPlayOne == rPlayTwo):
            points_one += 1
            points_two += 1
            print('Oh vaya, Ha sido un empate, por lo que agregaremos otra ronda')
            n_rondas += 1
            rondas += 1
    else:
        print(f'Puntos de {namePlayerOne}: {points_one}')
        print(f'Puntos de {namePlayerTwo}: {points_two}')
        if(points_one > points_two):
            print(f'{namePlayerOne} Ganó la partida')
        else:
            print(f'{namePlayerTwo} Ganó la partida')
dado_magico()
