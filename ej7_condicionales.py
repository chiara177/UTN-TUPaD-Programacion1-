frase = input("Ingrese una frase o palabra: ")
vocales = ("aeiouàèìòùAEIOUÀÈÌÒÙ")


if frase and frase[-1] in vocales:
    frase += "!"

print(frase)

