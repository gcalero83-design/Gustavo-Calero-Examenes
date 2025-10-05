"""
9.Escribir una clase Figura que debe tener un atributo de nombre de la figura.
Habrá otra clase llamada Rectangulo que hereda de Figura. Pedirá una base y una
altura en sus parámetros. Tendrá un método que devuelva el área y perímetro de este rectángulo.
También habrá otra clase llamada Circulo que hereda también de Figura, pedirá por parámetro el
radio y este tendrá los métodos que calculará el área y otro método que calculará el perímetro del círculo
Realizar la instancia de la clase figura mínimo 4 veces para mostrar el uso en ambas figuras
(2 casos para ambas figuras) y resultados de todos los métodos mediante consola.
"""
import math

class Figura:
    def __init__(self):
        self.nombre = input("Ingrese Nombre:")
class Rectangulo(Figura):
    def __init__(self):
        super().__init__()
        print("Ingrese parámetros del rectangulo:")
        self.base = float(input("ingrese base:"))
        self.altura = float(input("Ingreses altura: "))
    def area_rectangulo(self):
        area_rect= self.base * self.altura
        print("El area del rectangulo ",self.nombre," es: ", area_rect)
        return area_rect
    def perimetro_rectangulo(self):
        perimetro_rect = (self.base + self.altura) * 2
        print("El perímetro del rectangulo ",self.nombre," es: ", perimetro_rect)
        return perimetro_rect

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        print("Ingrese la base de la circulo:")
        self.radio = float(input("Ingrese radio: "))
    def area_circulo(self):
        area_circ = (self.radio) **2 * math.pi
        print("El area del circulo ",self.nombre," es: ", area_circ)
        return area_circ
    def perimetro_circulo(self):
        perimetro_circ = self.radio * 2 * math.pi
        print("El perímetro del circulo ",self.nombre," es: ", perimetro_circ)
        return perimetro_circ
Rectangulo1=Rectangulo()
Rectangulo2=Rectangulo()
Circulo1 = Circulo(4)
Circulo2 = Circulo(5)
print("\n--- Reporte de Calculos ---")
Rectangulo1.area_rectangulo()
Rectangulo1.perimetro_rectangulo()
Rectangulo2.area_rectangulo()
Rectangulo2.perimetro_rectangulo()
Circulo1.area_circulo()
Circulo2.area_circulo()
Circulo1.perimetro_circulo()
Circulo2.perimetro_circulo()






