buy_list = []
hola = True
conf_continue = 0
buy_objet = 0
miditch = {"name": "hola mundo", "altura": "2 metros"}
while hola:
    buy_objet = input("Que desea comprar?: ")
    buy_list.append(buy_objet)
    conf_continue = input(f"Se agregó {buy_objet}, Desea agregar otro producto?(Y/N): ")

    if conf_continue == "y":
        continue
    elif conf_continue == "n":
        hola = False
    else:
        print("Syntax Error")
else:
    print("Usted desea comprar:")
    for element in buy_list:
        print(element)
