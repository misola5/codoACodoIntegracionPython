# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def minComunMultiplo():
    '''
    función que calcula el mínimo común múltiplo entre dos números
    '''

    a=int(input("ingrese un numero: "))
    b=int(input("ingrese otro numero: "))
    c=min(a,b)
    d=max(a,b)
    e=a*b
    
    if d%c==0:
        mcm=d
    else:
        while e > d:           
            if e%c==0 and e%d==0:
                mcm=e
            e-=1
                            
        e-=1
        
    print(mcm)

minComunMultiplo()