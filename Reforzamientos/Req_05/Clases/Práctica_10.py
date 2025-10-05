"""
10.Crear una clase llamada Soldado para un juego sobre un mapa la cual deberá tener como atributos
 en el constructor posición X y posición Y las cuales iniciarán en 0, agregar un nombre a este soldado
 dentro de estos atributos.
La clase debe tener los siguientes métodos. Caminar hacia el eje X en donde se indicará cuántos pasos
dará y otra clase que le permitirá caminar por el eje Y, en caso se indique un número negativo indicar
 que solo puede llegar hasta el 0 si es menor a los pasos ya dados.
Crear finalmente un método adicional que irá guardando los pasos que ha dado dentro de una lista para
que finalmente al usar este método me muestre el historial de movimientos del Soldado, tanto en el eje X y en eje Y
Instanciar un mínimo de 5 movimientos para que muestre finalmente el historial de pasos de tu soldado
"""
class Soldado:
    def __init__(self, nombre, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.historial_movimientos = []

    def caminar_eje_x(self, pasos):
        self.posicion_x += pasos
        self.guardar_movimiento("X", pasos)
        print(f"{self.nombre} caminó {pasos} pasos en el eje X. Posición actual: ({self.posicion_x}, {self.posicion_y})")

    def caminar_eje_y(self, pasos):
        if pasos < 0 and self.posicion_y + pasos < 0:
            print(f"¡No se puede mover más allá del eje 0! Se ajusta la posición.")
            pasos_reales = -self.posicion_y
            self.posicion_y = 0
            self.guardar_movimiento("Y", -pasos_reales)
        else:
            self.posicion_y += pasos
            self.guardar_movimiento("Y", pasos)
        print(f"{self.nombre} caminó {pasos} pasos en el eje Y. Posición actual: ({self.posicion_x}, {self.posicion_y})")

    def guardar_movimiento(self, eje, pasos):
        self.historial_movimientos.append({
            "eje": eje,
            "pasos": pasos,
            "posicion_final": (self.posicion_x, self.posicion_y)})

    def mostrar_historial(self):
        print(f"\n--- Historial de movimientos para {self.nombre} ---")
        if not self.historial_movimientos:
            print("El soldado no ha realizado ningún movimiento.")
            return

        for movimiento in self.historial_movimientos:
            print(f"En el eje {movimiento['eje']}, dio {movimiento['pasos']} pasos. Posición final: {movimiento['posicion_final']}")

mi_soldado = Soldado("Rambo")

mi_soldado.caminar_eje_x(5)
mi_soldado.caminar_eje_y(3)
mi_soldado.caminar_eje_x(-2)
mi_soldado.caminar_eje_y(-4)
mi_soldado.caminar_eje_x(1)

mi_soldado.mostrar_historial()