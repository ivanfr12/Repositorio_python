print("*** Calculadora ***")

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    ''')
    opcion =int(input("Escoge una opcion: "))
    return opcion

def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    # Solicitamos los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: # sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2: # resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3: # multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4: # division
        resultado = operando1 / operando2
        print(f'El resultado de la division es: {resultado:.2f}\n')
    elif opcion == 5: # salir
        print('Saliendo del programa de Calculadora. Hasta pronto...')
        salir = True
    else:
        print('Opcion invalida. Seleccione otra opcion\n')
    return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)

