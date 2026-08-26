edad = int(input("Ingrese su edad: "))
if 1 <= edad <= 100:
    if edad < 12:
        print("Usted es niño/a")

    elif  12 <= edad < 18:
        print("Usted es adolescente")

    elif 18 <= edad < 30:
        print("Usted es adulto/a joven")

    elif edad >= 30:
        print("Usted es adulto/a")

else:
        print("Ingrese una edad valida")
