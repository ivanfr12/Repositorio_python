# Validacion de contraseña
# print("-- Creacion y Validadcion de contraseña --")
#
# password = input("Ingresa un password (debe tener al menos 6 caracteres)")
#
# # validacion de password
# while len(password) < 6:
#     print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
#     password = input('Ingresa un nuevo valor de password: ')
# print('El valor de password es valido')
# from cgi import print_form
# from itertools import product

# Adivinar un numero secreto
# print('--- Programa para adivinar un numero ---')
# from random import randint
# numero_secreto = randint(1, 50)
# intentos = 0
# INTENTOS_MAXIMOS = 5
# adivinanza = None
#
# while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
#     adivinanza = int(input('Adivina el número secretro entre (1 y 50)'))
#     intentos += 1
#     # Agregamos una guia para que sepa si el numero proporcionado fue mayor o menor
#     # que el numero secreto
#     if adivinanza < numero_secreto:
#         print('El número secreto es mayor')
#     elif adivinanza > numero_secreto:
#         print('El número secreto es menor')
# # Concluimos el juego
# if adivinanza == numero_secreto:
#     print(f'Felicitadades, adivinaste el número secreto en {intentos} intentos')
# else:
#     print(f'Lo siento, has agotado tus intentos maximos {INTENTOS_MAXIMOS}')
#     print(f'El numero secreto era: {numero_secreto}')

# Validacion de formularios
# print('*** Validacion de formularios ***')
# nombre_usuario = None
#
# while not nombre_usuario:
#     nombre_usuario = input('Ingresa tu nombre de usuario: ')
# print(f'Nombre de usuario valido: {nombre_usuario}')

# Ejemplos de ciclos for en py
# print('Repeticion de un mensaje')
#
# mensaje = input('Propociona un mensaje a repetir: ')
# numero_de_repeticiones = int(input('Proporciona el numero de repeticiones'))
#
# # Iterar sobre el rango de repeticiones
# for _ in range(numero_de_repeticiones):
#     print(mensaje)

# Dibujar un triangulo con ciclo for
# numero_de_filas = int(input('Propociona el numero de filas: '))
#
# # Iterar sobre cada fila de triangulo
# for fila in range(1, numero_de_filas + 1):
#     espacios_en_blanco = " " * (numero_de_filas - fila) # Calculo de la cantidad de espacios en blanco
#     caracteres = '*' * (2 * fila - 1) # calcular la cantidad de caracteres para la fila actual
#     print(f'{espacios_en_blanco}{caracteres}') # Imprimiendo espacios y asteriscos

# Iterar una cadena ciclo for
# cadena = 'Hola Mundo'
# for letra in cadena:
#     print(letra, end=' ')

# Listas en python las listas llevan corchetes [1,2,3,4,5]
# print('*** Listas en py ***')
# mi_lista = [1, 2, 3, 4, 5]
#
# # Accedemos a un elemento por indice
# print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
#
# # Modificamos el elemento de la lista
# mi_lista[1] = 10
# print(f'Modificamos el valor del indice 1: {mi_lista[1]}')
#
# # Agregar un nuevo elemento a la lista
# mi_lista.append(50)
# print(mi_lista)
#
# # Eliminar elementos de la lista
# del mi_lista[2]
# print(mi_lista)
#
# # Longitud de lista
# print(len(mi_lista))

# nombres = ["Karla","Juan", "Laura"]
#
# for nombre in nombres:
#     print(nombre)
#
# lista_heterogenea = [100, True, 'Ivonne']
# print()
# for elementos in lista_heterogenea:
#     print(elementos)

# Lista de reproduccion de canciones
# print("*** Programa de lista de canciones ***")
# # Aqui se define la lista
# lista_reproduccion = []
# numero_canciones = int(input('Cuantas canciones deseas agregar: '))
#
# # Iteramos cada elemento de la lista para agregar un nuevo elemento
# for indice in range(numero_canciones):
#     cancion = input(f'Proporciona la cancion {indice + 1}: ')
#     lista_reproduccion.append(cancion)
#
# # Empezamos a agregar canciones
# # lista_reproduccion.append('Dream on -Aerosmith')
# # lista_reproduccion.append('Hoteal California - Eagles')
# # lista_reproduccion.append('Staying ALive - Bee Gees')
#
# # ORdenar la lista en orden alfabetico
# lista_reproduccion.sort() # Orden ascendente
# #lista_reproduccion.sort(reverse=False) Orden Descendente
#
# # Mostrar la lista de canciones
# print(f'\n Lista de Reproduccion en orden Alfabetico: ')
# for cancion in lista_reproduccion:
#     print(f'- {cancion}')
#
# #print(f'Lista de canciones: {lista_reproduccion}')

# Ejercicio de promedio de calificaciones

# print('*** Aplicacion de promedio de calificaciones ***')
#
# total_calificaciones = int(input('Proporciona el n° de calificaciones a evaluar: '))
# calificaciones = []
#
# # iteramos la calificaciones
# for indice in range(total_calificaciones):
#     calificacion = int(input(f'Calificacion[{indice}] = '))
#     calificaciones.append(calificacion) # Agregamos la calificacion a la lista
#
# # Imprimimos las calificaciones proporcionadas
# print(f'\nLas calificaones proporcionadas son: {calificaciones}')
#
# # Calculamos el promedio de las calificaciones
# suma_calificaciones = sum(calificaciones)
# promedio = suma_calificaciones / total_calificaciones
# print(f'\n Promedio de las calificaciones: {promedio}')

# Tuplas
# print("\nManejo de tuplas")
# mi_tuplas = (1, 2, 3, 4, 5)
#
# for elemento in mi_tuplas:
#     print(elemento)
#
# # Crear una tupla para representar una coordenada x, y
# coordenadas = (3, 5)
#
# # Acceder a los elementos de la tupla
# print(f'Coordenada x: {coordenadas[0]}')
# print(f'Coordenada y: {coordenadas[1]}')
#
# # Desempaquetados de tuplas en py
# print("Desempaquedos de tuplas") # unpacking
#
# producto = ('P001', 'Camisa', 20.000)
#
# # Desempaquetamos cada valor en variales independientes
# id, descripcion, precio = producto
#
# print(f'Tuplas completa: {producto}')
# # Valores independientes ya desempaquetados
# print(f'Producto: id = {id}, descripción = {descripcion} precio = {precio}')

# print("*** Combinacion listas y tuplas ***")
#
# # Definir una lista que almacena tuplas de productos
# productos = [
#     ('P001', 'Camiseta', 20.000),
#     ('P002','Remera', 10.000),
#     ('P003', 'Jean', 30.000)
# ]
# # Imprimimos la informacion de cada producto
# # y calculamos el precio totoal
# precio_total = 0
#
# print(f'Informacion de los productos: ')
# for producto in productos:
#     #print(producto)
#     id, descripcion, precio = producto # unpacking
#     print(f'Producto: id = {id}, descripcion: {descripcion}, precio = {precio}')
#     precio_total += precio # productos[2] para obtener el precio
#
# print(f'Precio total de los productos: {precio_total}')

# Set (conjunto)
# print("-- Manejo de Sets --")
#
# # Crear un conjunto
# mi_set = {1, 2, 3, 4 ,5 , 4}
#
# print(f'mi set: {mi_set}')
#
# # Agregar elementos al conjunto
# mi_set.add(6)
# mi_set.add(7)
#
# # Intentear agregar un elemento duplicado
# mi_set.add(3)
# print(f'mi set: {mi_set}')
#
# # eliminar un elemento del conjunto
# mi_set.remove(4)
# print(f'mi set: {mi_set}')
#
# # Iterar los elementos de set
# for elemento in mi_set:
#     print(elemento, end=' ')
#
# # Comprobar si existe un elemento en el set
# print(f'\n{4 in mi_set}')
#
# # obtener la longitud
# print(len(mi_set))

# Boletin informativo
# print("---- Boletin de suscriptores ----")
#
# # DEfinimos el set inicial
# #suscriptores = {} aqui se esta defiiendo un diccionario vacio, esto no nos sirve
# suscriptores = set()
#
# numero_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
# for _ in range(numero_suscriptores):
#     suscriptores.add(input('Nuevo suscriptor (mail): '))
#
#
# print(f'Lista de suscriptores inicial: {suscriptores}')
#
# # Verificar si un nuevo suscriptor ya esta en la lista
# nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
# if nuevo_suscriptor in suscriptores:
#     print(f'El nuevo suscriptor ya esta en la lista: {nuevo_suscriptor}')
# else:
#     suscriptores.add(nuevo_suscriptor)
#     print(f'El nuevo suscriptor se ha agregado correctamente {nuevo_suscriptor}')
#
# # Eliminar un suscriptor existente
# suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
# suscriptores.remove(suscriptor_eliminar)
# print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
# print(f'Lista de suscriptores: {suscriptores}')
#
# # Verificar la cantidad total de suscriptores
# print(f'Cantidad total de suscriptores: {len(suscriptores)}')
#
# # Mostrar todos los suscriptores
# print(f'--- Lista de suscriptores ---')
# for suscriptor in suscriptores:
#     print(f'- {suscriptor}')

# dict - Diccionarios
# print(" --- Diccionario -----")
#
# # Crear un diccionario de persona con llave y valor
# persona = {'nombre': 'Sergio',
#            'Edad': 30,
#            'Ciudad': 'Mexico'}
# print(f'Diccionario de persona: {persona}')
#
# # Acceder a los elementos del diccionario
# print(f'Nombre: {persona['nombre']}')
# print(f'Edad: {persona['Edad']}')
# print(f'Ciudad: {persona['Ciudad']}')
#
# #Modificar un valor del dict
# persona['edad'] = 35
# print(f'Diccionario de persona: {persona}')
#
# # Agregar un nuevo elemento al dict
# persona['profesion'] = 'Ingeniero'
# print(f'Diccionario de persona: {persona}')
#
# # Eliminar un elemento del diccionario
# del persona['Ciudad']
# print(f'Diccionario de persona: {persona}')
#
# # iterar los elementos de un dict (llave, valor) (key-value)
# for clave, valor in persona.items():
#     print(f'Clave: {clave}, Valor: {valor}')

# Agenda de contactos utilizando diccionario con py
print('--- Agenda de contactos con dict en py ---')
agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'Carlos@mail.com',
        'direccion': 'calle principal 123'
    },
    "Maria": {
        "telefono": "998883300",
        "email": "maria@mail.com",
        "direccion": "calle Peru 01"
    },
    "Pedro": {
        "telefono": "0123489721",
        "email": "pedro@mail.com",
        "direccion": "calle perus1"
    }
}
print(agenda)
# for clave, valor in agenda.items():
#     print(f'Clave: {clave}, Valor: {valor}')

# Acceder a la informacion de un contacto
# print(f'''Información del contacto de María
#     Telefono: {agenda['Maria']['telefono']}
#     Email: {agenda['Maria']['email']}
#     Direccion: {agenda['Maria']['direccion']}
# ''')
#
# print(f'''Información del contacto de Carlos
#     Telefono: {agenda['Carlos']['telefono']}
#     Email: {agenda['Carlos']['email']}
#     Direccion: {agenda['Carlos']['direccion']}
# ''')
#
# print(f'''Información del contacto de Pedro
#     Telefono: {agenda['Pedro']['telefono']}
#     Email: {agenda['Pedro']['email']}
#     Direccion: {agenda['Pedro']['direccion']}
# ''')
#
# # Agregar un nuevo contacto
# agenda['Ana'] ={
#     'telefono': '556783418',
#     'email': 'ana@gmail.com',
#     'direccion': 'Calle Salvador 002'
# }
# print(agenda)
#
# # eliminar un contacto existen
# # del agenda['Pedro']
# # Podemos usar el metodo pop
# agenda.pop('Pedro')
# print(agenda)
#
# # Mostrar todos los contactos de la agenda
# print("\nLista de contactos en la agenda")
# for nombre, detalles in agenda.items():
#     print(f'''Nombre: {nombre}
#     Telefono: {detalles['telefono']}
#     Email: {detalles['email']}
#     Direccion: {detalles['direccion']}
# ''')

# Ejemplo de listas y diccionarios
# print('... Listas y diccionarios juntos ...')
#
# personas = [
#     {
#         "nombre": "Regina",
#         "apellido": "Flores",
#         "edad": 21
#     },
#     {
#         "nombre": "Leo",
#         "apellido": "Alarcon",
#         "edad": 25
#     }
# ]
# print(personas)
# # Acceder a un diccionario
# print(f'''Nombre: {personas[0].get('nombre')}
#     Apellido: {personas[0].get('apellido')}
#     Edad: {personas[0].get('edad')}
#
#     Nombre: {personas[1].get('nombre')}
#     Apellido: {personas[1].get('apellido')}
#     Edad: {personas[1].get('edad')}
# ''')
#
# # Recorrer los elementos de la lista
# for contador, persona in enumerate(personas):
#     print(f'Persona: {contador + 1}: {persona.get('nombre')}, {persona.get('apellido')}, {persona.get('edad')}')

# Sistema de gestion de inventarios
# print("----Programa de gestion de inventario-----")
# # Definimos la variable inventario
# inventario = []
#
# numero_productos = int(input("Cuantos productos deseas agregar al inventario? "))
#
# for indice in range(numero_productos):
#     print(f'Proporciona los valores del producto {indice + 1}')
#     nombre = input("Nombre: ")
#     precio = float(input('Precio: '))
#     cantidad = int(input('Cantidad: '))
#     # Crear el diccionario con el detalle del producto
#     producto = {'id': indice + 1, "nombre": nombre, 'precio': precio, 'cantidad': cantidad}
#     # Agregamos el nuevo producto al inventario
#     inventario.append(producto)
#
# # Mostrar el inventario de manera simplificada
# print(f'\n{inventario}')
#
# # Buscar un producto por ID
# id_buscar = int(input('\nIngresa el id del producto a buscar: '))
# producto_encontrado = None
# for producto in inventario:
#     if producto.get('id') == id_buscar:
#         producto_encontrado = producto
#         break
#
# if producto_encontrado:
#     print("Informacion del producto encontrado: ")
#     print(f'''Id: {producto_encontrado.get('id')}
#         Nombre: {producto_encontrado.get('nombre')}
#         Precio: {producto_encontrado.get("cantidad")}
#         Cantidad: {producto_encontrado.get("cantidad")}''')
# else:
#     print(f'Producto con id {id_buscar} no encontrado!')
#
# # Mostrar el inventario detallado
# print(f'\nInventario detallado actualizado: ')
# for producto in inventario:
#     print(f'''Id: {producto.get('id')}
#         Nombre: {producto.get('nombre')}
#         Precio: {producto.get("cantidad")}
#         Cantidad: {producto.get("cantidad")}''')


