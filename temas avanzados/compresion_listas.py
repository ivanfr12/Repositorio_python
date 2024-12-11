from functools import reduce

print("--- Compresion de Listas ---")

# Filtrar solo los numeros pares y generar una lista con estos valores

numeros = range(1, 10+1)
# Sin usar compresion de listas
numeros_pares = []
# Iterar cada elemento de la lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Numeros pares del 1 al 10: {numeros_pares}')

# Usando compresion de listas
# sintaxis: nueva_lista = [expresion for elemento in iterable if condicion]
numeros_pares = [numero**2 for numero in numeros if numero % 2 == 0]
print(f' numeros pares del 1 al 10: {numeros_pares}')

print("--- Funcion zip ----")
nombres = ['Juan', 'Maria', 'Pedro', 'Ana']
edades = [30, 25, 35, 20]
ciudades = ['Madrid', 'Barcelona', 'Sevilla', 'Corboba']

# Combinar los elementos correspondientes usando la funcion zip
personas = zip(nombres, edades, ciudades)

# Iterar sobre el resultado de la funcion zip
for persona in personas:
    print(persona)


# Maneja de cadenas funcion split
print("--- Funcion Split ---")
# Dividir una cadena split() (parsing)
cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

# Funcion find buscar y reemplazar
posicion = cadena.find('Mundo') # devolver el valor de 5
print(f'posicion de la cadena mundo: {posicion}')

# funcion replace - reemplazar
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicacion de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 3
print(f'Resultado multiplicacion de cadenas: {resultado_multiplicacion_cadenas}')

# Funcion strip - Eliminar espacio en blanco
cadena = '..Hola Mundo....'
cadena_limpia = cadena.strip('.')
print(f'Cadena limpia de caracteres al inicio y al final: {cadena_limpia}')

# Funciones lambda - funciones pequeñas y temporales
print('-- Funciones lambda ---')
# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2
print(f'El cuadrado de 5: {cuadrado(5)}')

# Funcion lambda (anonima)
cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 2: {cuadrado_lambda(2)}')
print(f'El cuadrado de 4: {cuadrado_lambda(4)}')

# Funciones map, filter con funciones lambda
print('--- Funciones map, filter junto con lambda ---')

# con map y lambda
# Creamos una lista de numeros
numeros = [1, 2, 3, 4, 5]

# Aplicar una funcion lambda para obetener el cuadrado de cada numero
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de usar filter para filrar numeros pares: {pares}')

# funcion reduce y map con lambda - reduce un valor

suma_acumalativa = reduce(lambda x, y: x + y, numeros)
print(f'Resultado de la suma aplicando reduce: {suma_acumalativa}')

# Ordenamiento de iterables (Sorted)
print('-- Ordenamiento en python --')
# Sintaxis : sorted(iterable, key=None, reverse=False)

empleados = ['Juan', 'Luis', 'Maria']
# ordenar la lista
#empleado_ordenados = sorted(empleados, reverse=True)
empleado_ordenados = sorted(empleados)
print(f'Empleados ordenados; {empleado_ordenados}')

# Ordenar un diccionario (una llave)
empleados_dict = [
    {'nombre': 'Juan', 'salario': 3000},
    {'nombre': 'Maria', 'salario': 2500},
    {'nombre': 'Pedro', 'salario': 3500}
]
#empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'], reverse=True)
empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'Empleados ordenados por salario: {empleados_ordenados_por_salario}')


# funciones Generadores en python
print('*** Generadores en Python ***')

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

# Creamos un generador
var_generador = generador(10)


# Iteramos sobre el generador
for valor in var_generador:
    print(valor)


# Expresiones generadoras
print('*** Expresiones Generadoras ***')

generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in generador:
    print(cuadrado_pares)

# Decoradores en python
print("-- Funciones o metodo deoradores")


def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar a la funcion de saludar')
        resultado = funcion(*args, **kwargs) # llamamos a nuestra funcion
        print('DEspues de llamar la funcion saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')

# Funcion sum() elementos iterables, funcion next
print("-- Funcion sum y next ---")
lista = [1, 2, 3, 4, 5]

# Suma de todos los elementos
resultado = sum(lista)
print(f"Resultado de la suma: {resultado}")

# Podemos proporcionar un valor inicial
resultado = sum(lista, 20)
print(f'Resultado de la suma inicial de 20: {resultado}')

# La funcion next - elementos de un iterador
iterador = iter(lista)

# Obtenemos el proximo elemento del iterador usando la funcion next
#elemento = next(iterador)
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')


# Excepciones en python
print("- Excepciones manejo -")
def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')

        resultado = numerador / denominador
        print(f' Resultado de la division: {resultado}')
    except Exception as e:
        print(f'Ocurrio un error\n: {e}')

    else:
        print(f'No ocurrio ningun error')

    finally:
        print(f'Terminamos de procesar la excepcion\n')
    # except ZeroDivisionError:
    #     print('Error: No se puede dividir entre cero')
    # except TypeError:
    #     print('Los operandos deben ser de tipo numericos')

# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')


# Manejo de archivos
# crear un archivo con python
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura ('w')
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola como estas\n')
    archivo.write('\nEstoy agregando informacion al archivo')

# archivo = open(nombre_archivo, 'w')
# archivo.write('Hola como estas\n')
# archivo.write('\nEstoy agregando informacion al archivo')
# archivo.close()

print(f'Se creo el archivo: {nombre_archivo}')