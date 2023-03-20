'''
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
'''
cadena=input("ingrese una cadena: ")
listaPalabras=cadena.split()
diccionarioFrecuencias={}

def palabraYFrecuencia():
    
    for palabra in listaPalabras:
        if  palabra in diccionarioFrecuencias:
            diccionarioFrecuencias[palabra] +=1
        else:
            diccionarioFrecuencias[palabra] = 1


def tuplaMasRepetida():
    # for palabra in listaPalabras:
    #     tuplaMasRepetida=diccionarioFrecuencias.get(palabra)
    #x=diccionarioFrecuencias
    #y=max(diccionarioFrecuencias.values())
    #p=diccionarioFrecuencias.values()
    o=diccionarioFrecuencias.items()

    for h in o:
        m=h
        print(m)
        print(type(m))
   
    # print(f"x es igual a {x}")
    # print(type(x))
    # print(f"y es igual a {y}")
    # print(f"o es igual a {o}")
    # print(type(o))
    
    
    # for a in diccionarioFrecuencias:
    #     print(a)
        
    # for w in p:
    #     print(w)

    


    #print(listaPalabras)
    #print(diccionarioFrecuencias[1])
    #print(tuplaMasRepetida)

palabraYFrecuencia()
tuplaMasRepetida()