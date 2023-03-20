'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos
'''

class Cuenta:
    
    def __init__(self, titular, cantidad):
        self._titular=titular
        self._cantidad=cantidad

    @property
    def titular(self):
        print(f"metodo getter para mostrar titular: {self._titular}")
        return self._titular
    
    @titular.setter
    def titular(self, nuevoTitular):        
       
        if nuevoTitular.length <= 0:
            print("Debe ingresar un usuario")
        else:
            print(f"Este setter permite ingresar un titular: {self._titular}")
            self._titular=nuevoTitular

        return self._titular
        
    @property
    def cantidad(self):
        print(f"metodo getter para mostrar cantidad: {self._cantidad}")
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nuevaCantidad):
        self._cantidad=nuevaCantidad
        print(f"Este setter permite ingresar un saldo inicial: {self._cantidad}")
        return self._cantidad

    def mostrar(self):
        print(self._titular)
        print(self._cantidad)

    def __str__(self):
        return f"El titular de la cuenta es: {self._titular} y su saldo es: ({self._cantidad})"
    
    def ingresar(self):

        ingreso=float(input("¿Cuanto dineron desea ingresar? "))

        if ingreso > 0:
            self._cantidad=self._cantidad+ingreso
        else:
            self._cantidad=self._cantidad
        print(f"Su saldo actual es: {self._cantidad}")
        return self._cantidad

    def retirar(self):
        retiro=float(input("¿Cuánto dinero desea retirar?"))
        self._cantidad=self._cantidad-retiro
        print(f"Su saldo actual es: {self._cantidad}")
        return self._cantidad

# def nuevaCuenta():
#     nombre=input("ingrese un nombre de cuenta: ")
#     nombre.titular=input("nombre del usuario: ")
#     nombre.cantidad=float(input("ingrese una cantidad inicial: "))
#     nombre=Cuenta({nombre.titular}, {nombre.cantidad})
    


# nuevaCuenta()
'''
quise crear una funcion para hacer una cuenta nueva y no me salió
'''



# p1=Cuenta("marcelo", 200)
# p1.mostrar()
# print(p1)
# p1.ingresar()
# print(p1)
# p1.retirar()
# print(p1)