#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#   cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

a=input("ingrese una cadena: ")
b=a.split()

diccionarioFrecuencias = {}
for palabra in b:
    if palabra in diccionarioFrecuencias:
        diccionarioFrecuencias[palabra] += 1
    else:
        diccionarioFrecuencias[palabra] = 1

print(diccionarioFrecuencias)