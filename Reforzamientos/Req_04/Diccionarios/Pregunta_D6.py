"""
6.Ingresar por consola 4 números mediante consola, crear un diccionario donde los ‘key’ serán los números indicados
 y los valores serán los cubos de las estos keys. Mostrar finalmente este diccionario.
"""
cubos={}
num1=input('ingresa un número:')
num2=input('ingresa un número:')
num3=input('ingresa un número:')
num4=input('ingresa un número:')
cubos['1']=int(num1)**3
cubos['2']=int(num2)**3
cubos['3']=int(num3)**3
cubos['4']=int(num4)**3
print('Mi diccionario es:',cubos)