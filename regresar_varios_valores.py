

print('*** Regresar una tupla de valores desde una funcion ***')

# Definicion de la funcion
# def persona_mayusculas(nombre, apellido, edad):
#     print('Esta funcion regresa varios valores (tupla)')
#     return nombre.upper(), apellido.upper(), edad
#
# # programa principal
# nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
# print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')
#
# # Tuplas
# print('-- Obtener coordenadas --')
#
# def obtener_coordenadas():
#     x, y , z = 10, 20, 30
#     #return (x, y, z ) # No hay necesidad de usar parentesis para definir la tupla
#     return x, y, z
#
# # LLamar la funcion
# resultado = obtener_coordenadas()
# print(resultado)
#
# # Unpacking de la tupla
# x1, y1, z1 = resultado
#
# # Imprimir los valores de manera individual
# print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')

# Argumentos variables en python
# print('--- Argumentos variables ---')
#
# def superheroes_superpoderes(superheroe, nombre, *args):
#     print(f'Superheroe: {superheroe} - {nombre} - {args}')
#     # Iteramos los superporderes
#     for superpoder in args:
#         print(f'\tSupoder: {superpoder}')
#
# # LLAMAR A LA FUNCIONM
# superheroes_superpoderes('Spiderman', 'Peter Parker', 'Instinto aracnido', 'Telaraña')
# superheroes_superpoderes('Ironman', 'Tony Stark','Armadura', 'Playboy', 'Millonario')
#
# # Es opcional enviar argumentos variables
# superheroes_superpoderes('Mi vecino', 'Juan Perez')


# args - arguments - tupla
# Kwargs_argumentos
# Kwargs -keyword arguments (key, value)
# print(' --- Argumentos variables por llave ---- ')
#
# def superheroe_superpoderes(nombre, *args, **kwargs):
#     print(f'Superheroe: {nombre} - {args}. Mas info: {kwargs}')
#
# # LLAMAMOS LA FUNCION
# superheroe_superpoderes('Spiderman', 'Instinto Aracnido', edad=17, empresa='Marvel')
# superheroe_superpoderes('Ironman', 'Armadura','Playboy', edad=45)
# # ES opcional argumentos varabiles
# superheroe_superpoderes('Mi vecino', personalidad='buena onda')

# print('Suma con argumentos varibles')
# # Funcion sumar que acepta argumentos variables
# def sumar(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total
#
# # Llamamos la funcion sumar
# resultado = sumar(1, 2 ,3 , 4 , 5, 6, 7 ,8, 9)
# print(f'Resultado de la suma: {resultado}')

# Imprimir info clave valor
# print('usando kwargs para imprmir informacion')
# # funcion que acepta argumentos variables de tipo llave valor
# def imprimir_info(**kwargs):
#     print(f'\nValores recibidos:')
#     for llave, valor in kwargs.items():
#         print(f'{llave}:{valor}')
# # llamamos a la funcion
# imprimir_info(nombre='Karla', edad=30, ciudad='Mexico')
# imprimir_info(nombre='Carlos', edad=28, ciudad='Us')
# imprimir_info(nombre='Jose', edad=20, ciudad='Uruguay')

# Funcion es par
# print("Funcion par")
# # funcion para saber si un numero es par o no
#
# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
#
# # LLAMAMOS A LA FUNCION
# if __name__ == '__main__':
#     numero = int(input('Ingresa un valor numero: '))
#     print(f'Numero par? {es_par(numero)}')

# funciones recursivas
# print('-- Funciones recursivas --')
# print("Imprimir del 1 al 5 de forma recursiva")
#
# # DEfinimos la funcion recursiva
# def funcion_recursiva(numero):
#     # caso base
#     if numero == 1:
#         print(numero, end=' ')
#     else: # Caso recursivo
#         funcion_recursiva(numero - 1)
#         print(numero, end=' ')
#
#
# # Programa principal
# if __name__ == '__main__':
#     funcion_recursiva(10)


# Factorial de 5!
# print("--- Factorial del numero 5 recursivas ---")
#
# # Definir la funcion factorial recursiva
# def factorial_recursivo(numero):
#     # caso base: factorial de 0 o 1 es 1
#     if numero == 0 or numero == 1:
#         print(f'Resultado factorial parcial {numero} es: 1')
#         return 1
#     # caso recursivo, calcular factorial del numero reducido en 1
#     else:
#         factorial_parcial = numero * factorial_recursivo(numero - 1)
#         print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
#         return factorial_parcial
#
# # Programa principal
# if __name__ == '__main__':
#     # Solicitar al usuario el numero del cual desea calcular el factorial
#     numero = int(input("Proporciona el numero para calcular su factorial: "))
#     # Verificamos el numero
#     if numero < 0:
#         print("El factorail no esta definido para numeros negativos")
#     else:
#         # llamamos a la funcion factorial_recursivo para calcular el factorial
#         resultado = factorial_recursivo(numero)
#         print(f'El factorial de {numero} es: {resultado}')

# Sistema de inventario con sistema de funciones
print("--- sistema de inventarios con funciones ----")
# Inventario del almacen

inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# funcion para mostrar el inventario
def mostrar_inventario():
    print('Inventario del almacen')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

# Funcion para agregar un nuevo producto
def agregar_producto():
    # pass # Pasa por esta funcion, sin ejecutar nada mas
    print('--- Agregar nuevo producto ---')
    id = int(input('Id: '))
    nombre = input("Nombre: ")
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre': nombre,
                    'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')


# Funcion para buscar por id
def buscar_producto_por_id():
    print('--- Buscar Producto por id ---')
    id_buscar = int(input('Ingresa el ID a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print(f'\nInformacion del producto encontrado: ')
            print(f'ID: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f'Precio: ${producto.get('precio')},'
                  f'Cantidad: {producto.get('cantidad')}')
            return
        print('\nProducto no encontrado')

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n --- Menu ---
        1. Mostrar inventarios
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir
''')
        opcion = int(input('Prporciona una opcion (1-4): '))
        # REvisamos las opciones del menu
        if opcion == 1: # Mostrar inventario
            mostrar_inventario()
        elif opcion == 2: # Agregar nuevo producto
            agregar_producto()
        elif opcion == 3: # Buscar productos por id
            buscar_producto_por_id()
        elif opcion == 4:
            print('Hasta luego!')
            break
        else:
            print('Proporciona una opcion valida')