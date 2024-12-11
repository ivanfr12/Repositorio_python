#import modulo_funcion_sumar

from modulo_funcion_sumar import sumar



print("_--- Funciones en python ---_")


# 1. Definir una funcion llamada saludar
def saludar(mensaje):
    print(f'Mensaje recibido: {mensaje}')
    return 'Termino ok la ejecucion de la funcion saludar'


# 2. Llamar la funcion (ya que tiene que estar definida)
argumento = 'Hola desde la funcion saludar'
valor_devuelto = saludar(argumento)
print(f'Valor devuelto de la funcion: {valor_devuelto}')


if __name__ == '__main__':
    # funcion sumar
    print(" Funcion sumar")

    # definicion sumar
    def sumar(a, b):
        resultado = a + b
        return resultado

    # LLamamos a la funcion saludar
    # arg1, arg2 = 5, 7
    arg1 = float(input('Ingresa el argumento 1: '))
    arg2 = float(input('Ingresa el argumento 2: '))
    resultado_suma = sumar(arg1, arg2)
    print(f'REsultado suma: {resultado_suma}')
