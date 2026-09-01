
numero1= int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

menor = min(numero1, numero2)
mayor = max(numero1, numero2)

suma = 0

for i in range(menor + 1, mayor):
    suma += i

print(f"La suma de los numeros que estan entre {numero1} y {numero2} es {suma}")


