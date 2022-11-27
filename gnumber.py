import random
random_num=random.randrange(0,100,1)
print(random_num)
r_state=False
beggin=input('Desea jugar a Adivina el numero?(Y/N): ')
if(beggin=='Y'):
    r_state=True
while(r_state==True):
    global r_quest
    r_quest=int(input('Ingrese un numero del 1-100: '))
    if(r_quest == random_num):
        print('Eres el mejor, acertaste')
        break
    else:
        print('Que lastima, intenta de nuevo')
        continue
else:
    print('Que triste, será la proxima vez')