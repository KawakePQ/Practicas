try:
    a=input("Inserte valor de A: ")
    b=input("Inserte valor de B: ")
    c=input("Inserte valor de C: ")
    a=int(a) 
    b=int(b)
    c=int(c)
    b_2=b**2
    ac_4=a*c*4
    a_2=a*2
    x_1=(-b+((b_2-ac_4)**0.5))/a_2
    print(x_1)
    x_2=(-b-((b_2-ac_4)**0.5))/a_2
    print(x_2)
except Exception as E:
    print(E)
    
    
