
suma = 0

numero = int(input("Ingrese un numero (0 para terminar): "))

while numero != 0:
    suma += numero
    print("Ingrese un numero (0 para terminar): ")
    numero = int(input())

print("El total es:",suma)

        