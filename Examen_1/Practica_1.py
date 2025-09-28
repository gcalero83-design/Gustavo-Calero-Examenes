"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""
Nombre=str("Gustavo Calero")
Salario=3500
Edad=str(42)
Compañia="Inversiones Pepito "
if int(Edad) >=30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    print("Bono Final es :", Salario ** 2 + Salario * .10)
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    print("Bono Final es :",Salario**2 + Salario*.05)
print("Tipo de Variable de Nombre es:", type(Nombre))
print("Tipo de Variable de Salario es:", type(Salario))
print("Tipo de Variable de Edad es:", type(Edad))
print("Tipo de Variable de Compañia es:", type(Compañia))
dic={"a":1,"b":2,"c":3,"d":4,"e":5}
print(dic)

