#Calculo del seno de un angulo
try:
    angle=input("Inserte Angulo:")
    x=int(angle)
    a=180-x
    num=4*x*a
    den=40500-(x*a)
    sinx=num/den
    print(sinx)
    print(round(sinx,4))
except Exception as E:
    print(E)
