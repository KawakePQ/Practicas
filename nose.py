hay_repetidos = lambda my_str: len(my_str) != len(list(set(my_str)))
print(hay_repetidos("hola"))
print(hay_repetidos("holaa"))
