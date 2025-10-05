"""
4.Crear una clase Alumno que tenga como atributos el nombre, edad y la nota final del alumno.
Crear los métodos para inicializar sus atributos, otro para imprimirlos y un método para mostrar
un mensaje con el resultado de la nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar
 la clase por lo menos 4 veces (4 alumnos)
"""
class Alumno:
    def __init__(self, nombre="", edad=0, nota_final=0):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota Final: {self.nota_final}")
lista_alumnos = []
contador = 0
while contador < 4:
    print(f"\n--- Ingresando alumno #{contador + 1} ---")
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    nota_final = float(input("Ingrese la nota final del alumno: "))


    nuevo_alumno=Alumno(nombre, edad, nota_final)
    lista_alumnos.append(nuevo_alumno)
    contador += 1
for alumno in lista_alumnos:
    alumno.mostrar_datos()
print("Ingreso de datos finalizado")



