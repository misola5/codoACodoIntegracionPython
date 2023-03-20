

# 1. Escribir una función que calcule el máximo común divisor entre dos números

def mcd():
    '''
     _-*    calcula el máximo común divisor entre dos números   *-_
    '''
    
    a=int(input("ingrese un numero: "))
    b=int(input("ingrese otro numero: "))
    max=1
    i=1
    c=min(a,b)

    while i <= c:
        if a % i==0 and b % i == 0:
            max=i
        i+=1
        
    print(max)

mcd()