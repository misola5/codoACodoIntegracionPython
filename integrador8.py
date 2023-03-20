'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
'''
from integrador7 import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad)
        self._bonificacion=bonificacion
        self._edad=edad

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nuevaBonificacion):
        self._bonificacion=nuevaBonificacion

    def __str__(self):
        return f"Cuenta joven, la bonificacion es {self._bonificacion}"
    
    def titularValido(self):

        self._edad:int(input("Ingrese su edad: "))

        if self._edad>18 and self._edad<24:
            return True
        else:
            print("El titular no tiene bonificaciones")
            return False
        
    def retirar(self):
        retiro=float(input("¿Cuánto dinero desea retirar?"))
        
        if self.titularValido():
            self._cantidad=self._cantidad-retiro
            print(f"Su saldo actual es: {self._cantidad}")
        else:
            print("No es posible hacer el retiro de dinero, su saldo es {self._cantidad}")
        return self._cantidad
    
c2=CuentaJoven("Marcelo", 500, 20, 20)
print(c2)
c2.titularValido()
c2.retirar()