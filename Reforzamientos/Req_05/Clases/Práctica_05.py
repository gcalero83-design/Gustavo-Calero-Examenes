"""
5.Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar
si la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo, en caso sea mayor de edad.
Un método para saber cuántos meses ha estado trabajando en la empresa
Instanciar por lo menos la clase con 3 diferentes personas.
"""
class Persona:
    def __init__(self, nombre, edad, sueldo, mes_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.mes_trabajados = mes_trabajados
#print("Ingresar datos solicitados")
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        #print(f"Meses Trabajando: {self.meses_trabajados}")
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
    def calcular_bonificacion(self):
        if self.edad >= 18:
            bonificacion = self.sueldo * 0.20
            print("El bonificacion es: ", bonificacion)
            return bonificacion
        else:
            print("No aplica bonificación para menores de edad")
    def meses_trabajados(self):
        print("Ha trabajado por ", self.mes_trabajados)

persona1=Persona("Ana Lopez",25,2500,12)
persona2=Persona("Juan Pérez",17,1200,3)
Persona3=Persona("María García",30,3500,24)
persona1.mostrar_datos()
persona1.calcular_bonificacion()
persona1.meses_trabajados()
