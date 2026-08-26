import random
from statistics import mean, median, mode

numero_aleatorio = [random.randint(1,100) for i in range(50)]

media = mean(numero_aleatorio)
mediana = median(numero_aleatorio)
moda = mode(numero_aleatorio)

print(f""" 
Media: {media}
Mediana: {mediana}
Moda: {moda}""")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")

elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")

elif media == mediana and mediana == moda:
    print("Sin sesgo")

else:
    print("No se llegan a cumplir las condiciones")