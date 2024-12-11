from encodings.punycode import selective_find

print("--- Creacion de clases aritmeticas ---")

class Aritmetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado de resta: {resultado}')


    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado de multiplicacion: {resultado}')


    def division(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado de division: {resultado}')


    # Metodos get / set
    def get_operando1(self):
        return self._operando1

    def set_operando1(self, operando1):
        self._operando1 = operando1

    def get_operando2(self):
        return self._operando2

    def set_operando2(self, operando2):
        self._operando2 = operando2


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo clase aritmetica ***')
    print('Objeto aritmetica 1')
    aritmetica1 = Aritmetica(5, 7)
    print(f'Valor Operando1 del objeto aritmetica1: {aritmetica1.get_operando1()}')
    print(f'Valor Operando2 del objeto aritmetica1: {aritmetica1.get_operando2()}')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segungo objeto
    print('\nObjeto aritmetica 2')
    aritmetica2 = Aritmetica(10, 5)
    print(f'Valor Operando1 del objeto aritmetica2: {aritmetica2.get_operando1()}')
    print(f'Valor Operando2 del objeto aritmetica2: {aritmetica2.get_operando2()}')
    aritmetica2.set_operando1(10)
    aritmetica2.set_operando2(15)
    aritmetica2.sumar()
    aritmetica2.restar()
