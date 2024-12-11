print('*** Funcion con argumentos por nombre ***')

def crear_persona(nombre, apellido='', edad=0):
    print(f'Persiona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

#crear_persona('Ricardo', 'Ronaldo', 23)
#crear_persona(edad=32, apellido='Fernandez',nombre='JOrge')
crear_persona(apellido='Fernandez',nombre='Jorge')