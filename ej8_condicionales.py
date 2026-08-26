
print(""" 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro""")

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opcion que desea: "))

if opcion == 1:
    print(nombre.upper())

elif opcion == 2:
    print(nombre.lower())

elif opcion == 3:
    print(nombre.title())

else:
    print("Ingrese una opcion valida")

