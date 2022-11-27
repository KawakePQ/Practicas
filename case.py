num_1=int(input("Primer Numero: "))
num_2=int(input("Segundo Numero: "))
oper=input("Ingrese tipo de operación(+,-,/,*): ")
match oper:
    case "+":
        result=num_1+num_2
        print(f'Su resultado es: {result}')
    case "-":
        result=num_1-num_2
        print(f'Su resultado es: {result}')
    case "/":
        result=num_1/num_2
        print(f'Su resultado es: {result}')
    case "*":
        result=num_1*num_2
        print(f'Su resultado es: {result}')   
    case _:
        print("Syntax Error") 