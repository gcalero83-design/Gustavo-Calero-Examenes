"""
3.Crear una función funciona_indice(persona, indice) y dentro la respectiva excepción para el siguiente bloque de código para
que tu programa no se bloquee y además imprime un mensaje al usuario: “El índice “nombre_indice” ingresado no existe en el diccionario”,
tipo de datos, etc que más pueden incurrir para este caso (los datos se pedirán por consola):
persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'} persona['profesion'] #El índice en este caso no existe
Usar la función al menos 2 veces incluyendo un caso de error
"""
datos = {'nombre':'Gustavo','apellido':'Calero','dni':'41836893'}

def funcion_indice(dic, indice):
    try:
        print(f"Valor de '{indice}':", dic[indice])
    except KeyError:
        print(f"Error: El índice '{indice}' ingresado no existe en el diccionario")
    except TypeError:
        print("Error: El índice debe ser de tipo string")


print("Caso 1: válido")
funcion_indice(datos, "nombre")

print("\nCaso 2: índice que no existe")
funcion_indice(datos, "profesion")