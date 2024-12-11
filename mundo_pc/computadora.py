from mundo_pc.dispositivo_entrada import DispositivoEntrada
from mundo_pc.monitor import Monitor
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._teclado = teclado
        self._raton = raton
        self._monitor = monitor


    def __str__(self):
        return f'''{self._nombre}: {self.id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}'''

# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 27)
    computadora1 = Computadora('Dell', teclado1, raton1, monitor1)
    print(computadora1)

    teclado2 = Teclado('Gamer', 'Bluuetooh')
    raton2 = Raton('Gamer', 'Bluuetooh')
    monitor2 = Monitor('Gamer', 34)
    computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
    print(computadora2)