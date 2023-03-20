'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

'''

class Persona:

    def __init__(self, nombre, edad, dni):
        self._nombre=nombre
        self._edad=edad
        self._dni=dni

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre=nuevoNombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nuevaEdad):
        self._edad=nuevaEdad

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, nuevoDni):
        self._dni=nuevoDni

    def __str__(self):
        return f"La cuenta pertenece a {self.nombre} de {self.edad} años con DNI N° {self.dni}"

    def esMayorDeEdad(self):
        if self.edad>18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self._nombre} no es mayor de edad.")

marcelo=Persona("Marcelo", 40, 29801894)
print(marcelo)
marcelo.esMayorDeEdad()
marcelo.edad=16
print(marcelo)
marcelo.esMayorDeEdad()