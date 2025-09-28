"""
2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""
def normalizar_nombres(nombres):
    nombres_procesados = []
    nombres_vistos = set()

    for nombre_completo in nombres:
        nombre_limpio = nombre_completo.strip()
        partes_nombre = nombre_limpio.title().split()
        for nombre_individual in partes_nombre:
            if nombre_individual not in nombres_vistos:
                nombres_procesados.append(nombre_individual)
                nombres_vistos.add(nombre_individual)
    return nombres_procesados
lista_nombres_original = [
    "  juan perez ",
    "maria    gonzalez",
    "juan perez",
    "luis fernando gomez",
    "ana maria lopez",
    " MARÍA DEL CARMEN ",
    "ANTONIO SOLER",
    "ana maria lopez",
    "pedro",
    "MARÍA DEL CARMEN LOZANO"
]

nombres_normalizados = normalizar_nombres(lista_nombres_original)
print(f"Lista original: {lista_nombres_original}")
print(f"Nombres normalizados: {nombres_normalizados}")