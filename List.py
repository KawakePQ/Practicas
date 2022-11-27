init=input("Desea hacer una lista de compras?(Y/N): ")
p_list=[]
c_list=[]
b_int=0
c_int=0
exit_state=0
init_state=False
if(init == "Y"):
    init_state=True;
else:
    print("Vuelva más tarde")
while(init_state == True):
    b_int=input('Que producto desea comprar?: ')
    p_list.append(b_int)
    c_int=input('QUe cantidad desea comprar?: ')
    c_list.append(c_int)
    exit_state=input('Desea añadir otro producto?(Y/N): ')
    if(exit_state == 'N'):
        init_state=False
else:
    print('Vuelva pronto')
    print('Usted desea comprar:')
    for product, cant in zip(p_list,c_list):
        print(cant,product)

