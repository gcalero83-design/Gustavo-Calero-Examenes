"""
6.Crear una clase PersonaPrestamo que hereda de la clase anterior (problema 5) donde tendrá los métodos:
Uno, que indicará si la persona está apta para un préstamo solo si ha estado más de 12 meses trabajando
en la empresa en caso contrario se le informa que no es posible darle el préstamo y la otra condición
adicional es si su edad es mayor de 25 años.
Agregar un segundo método a esta nueva clase que te indicará si estás aprobado recibirás 10 veces tu
sueldo de préstamo, el total de préstamo otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados.
"""
class Persona:
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_trabajados = meses_trabajados

class PersonaPrestamo(Persona):

    def evaluar_prestamo(self):
        if self.edad > 25 and self.meses_trabajados > 12:
            print(f"{self.nombre} está apto para el préstamo")
            return True
        else:
            print(f"{self.nombre} no cumple los requisitos")
            return False

    def monto_prestamo(self):
        if self.evaluar_prestamo():
            cantidad_prestamo = self.sueldo * 10
            print(f"El total del préstamo otorgado es: {cantidad_prestamo} soles")
        else:
            print("No se puede calcular préstamo.")
p1 = PersonaPrestamo("Gustavo", 35, 3500, 12)
p2 = PersonaPrestamo("Antonella", 32, 2200, 15)
p3 = PersonaPrestamo("Karla", 26, 2800, 25)


print("\n--- RESULTADOS ---")
p1.monto_prestamo()
print()
p2.monto_prestamo()
print()
p3.monto_prestamo()
