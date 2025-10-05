"""
7.Desarrolla una clase Agenda que administrará contactos. Dentro de una lista se debe almacenar
un diccionario para cada contacto el nombre, el teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI) Estructura de la lista cada vez que vas
agregando un contacto: contactos = [{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’: 44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’: “milagros19c@gmail.com”, ‘dni’: 43423211}
]
Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar la búsqueda de estas
personas en la agenda y saber si existen, en caso contrario indicar: “´Nombre´ no se encuentra anotado en la agenda”
"""
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni}
        self.contactos.append(contacto)
        print(f"Contacto {nombre} agregado correctamente.\n")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.\n")
        else:
            print("Lista de contactos:")
            for c in self.contactos:
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}")
            print()

    def buscar_contacto(self, dni):
        for c in self.contactos:
            if c['dni'] == dni:
                print(f"Contacto encontrado: {c['nombre']}")
                print(f"Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}\n")
                return
        print(f"El contacto con DNI {dni} no se encuentra anotado en la agenda.\n")


mi_agenda = Agenda()

mi_agenda.añadir_contacto("Luis", "997667945", "luishh@gmail.com", 44234239)
mi_agenda.añadir_contacto("Milagros", "997654687", "milagros19c@gmail.com", 43423211)
mi_agenda.añadir_contacto("Pedro", "987654321", "pedro23@gmail.com", 42345678)
mi_agenda.añadir_contacto("Ana", "912345678", "anaq@gmail.com", 45678901)

mi_agenda.mostrar_contactos()

mi_agenda.buscar_contacto(43423211)  # Existe
mi_agenda.buscar_contacto(99999999)  # No existe
