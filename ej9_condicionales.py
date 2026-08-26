magnitud = int(input("Ingrese la magnitud del terremoto: "))
#● Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

if magnitud < 3:
    print("Muy leve, imperceptible")

elif 3 <= magnitud < 4:
    print("Leve, ligeramente perceptible")

elif 4 <= magnitud < 5:
    print("Moderado, sentido pero no causa daños generalmente")

elif 5 <= magnitud < 6:
    print("Fuerte, puede llegar a causar daños")

elif 6 <= magnitud < 7:
    print("Muy fuerte, puede causar daños significativos")

elif magnitud >= 7:
    print("Extremo, causa daños a gran escala en la mayoria de los casos")