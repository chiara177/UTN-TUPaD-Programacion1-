numero = int(input("Ingrese el numero que quiere invertir: "))

invertido = 0

original = numero

while numero > 0:
    digito = numero % 10
    invertido = (invertido * 10) + digito
    numero = numero // 10


print("*" * 20)
print("Numero original:",original)
print("Numero invertido:",invertido) 