CANT = 10

suma = 0

for i in range(CANT):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / CANT

print("-" * 20)
print("Suma total:",suma)
print("La media de los", CANT, "números es:", media)
