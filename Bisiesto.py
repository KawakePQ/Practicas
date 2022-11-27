year=int(input('Ingrese año: '))
calc_a=year%4
calc_b=year%100
print(calc_a)
print(calc_b)
if (calc_a == 0 and calc_b != 0):
    print('Tu año es bisiesto')
else:
    print('Tu año es normal')
