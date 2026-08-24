# UTN-TUPaD-Programacion1-
#Ejercicio 1

print("Hola mundo!")

print("////////")


#Ejercicio 2

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

print("////////")


#Ejercicio 3

nombre =input("Porfavor ingrese su nombre: ")
print(f"Hola {nombre}")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Y su lugar de resicdencia: ")

print(f"Hola soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

print("///////")

#Ejercicio 4

radio = float(input("Ingrese el radio de un circulo: "))

area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f""" 
El radio del circulo es: {radio}
Su area: {area:.2f}
Y su perimetro: {perimetro:.2f}""")

print("///////")

#Ejercicio 5

segundos = int(input("Ingrese un a cierta cantidad de segundos: "))

horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas")

print("///////")

#Ejercicio 6

numero = int(input("Ingrese el numero del que desea saber la tabla de multipicar: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

print("///////////")

#Ejercicio 7

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 // numero2

print(f""" 
suma: {suma}
resta: {resta}
multiplicacion: {multiplicacion}
division: {division}""")

print("///////////")

#Ejercicio 8

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso // (altura ** 2)
print(f"Su indice de masa corporales: {imc}")

print("/////////")

#Ejercicio 9

grados_celsius = float(input("Ingrese la temperatura en grados celsius: "))

grados_farenheit = 1.8 * grados_celsius + 32

print(f"{grados_celsius} grados celsius equivalen a {grados_farenheit} grados farenheit")

print("//////////")

#Ejercicio 10

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))
numero3 = int(input("Ingrese un tercer numero: "))

suma = numero1 + numero2 + numero3
promedio = suma / 3

print(f"El promedio de dichos numeros es:{promedio:.2f} ")