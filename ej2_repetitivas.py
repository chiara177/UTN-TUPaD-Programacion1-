numero = input("Ingrese un numero entero: ")

while not numero.isdigit():
    print("Ingrese un numero positivo")
    numero = input()

cantidad_digitos = len(numero)
print(f"El numero tiene {cantidad_digitos} digito(s).")