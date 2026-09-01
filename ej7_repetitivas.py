limite = int(input("Ingrese su numero limite: ")) 
suma = 0

for i in range(0,limite +1):
    suma += i
print("La suma de todos los numeros del 0 al", limite, "es: ",suma)