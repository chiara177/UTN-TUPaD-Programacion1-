import random

numero_aleatorio = random.randint(0,9)

cont = 0

numero_usuario = -1

print("Averigue el numero entre 0 y 9")

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("ingrese un numero: ",))
    cont += 1
    
    if numero_usuario < numero_aleatorio:
        print("Es más alto")
    elif numero_usuario > numero_aleatorio:
        print("Es más bajo")
        
print(f"Acertaste el numero era {numero_aleatorio} y te tomo {cont} intentos, Felicitaciones!")