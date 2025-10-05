"""
3.Crear un decorador conteo_parametros(funcion) donde imprimirá la cantidad de argumentos que tiene la
función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es” mensaje post “La función decoradora
terminó de ejecutarse correctamente”
Ejemplo: Al usar una función suma que creamos: suma(4, 1, 10, 2, 50, 64)
Salida:
“La cantidad de argumentos que tiene la función es 5”
“La función decoradora terminó de ejecutarse correctamente”
Consideración:
Todos los parámetros ingresados deben ser enteros, caso sean String alguno de ellos indicar al usuario:
“Solo está admitido datos enteros, no se podrá realizar la suma”
Usar la función al menos 3 veces
"""
def conteo_parametros(funcion):
    def decorador_interno(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma.")
                return

        for key, value in kwargs.items():
            if not isinstance(value, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma.")
                return

        print(f"La cantidad de argumentos que tiene la función es {len(args) + len(kwargs)}")

        resultado = funcion(*args, **kwargs)

        print("La función decoradora terminó de ejecutarse correctamente.")
        return resultado
    return decorador_interno

@conteo_parametros
def suma(*args):

    return sum(args)

print("--- Primer uso ---")
suma(4, 1, 10, 2, 50, 64)

print("\n--- Segundo uso ---")
suma(1, 2, 3)

print("\n--- Tercer uso (con un argumento no entero) ---")
suma(10, 5, "hola", 20)