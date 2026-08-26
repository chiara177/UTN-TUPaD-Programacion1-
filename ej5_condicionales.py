contraseña = input("Ingrese una contraseña (8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Su contraseña es correcta")

else:
    print("Ingrese una contraseña entre 8 y 14 caracteres")