from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton
print('*** Mundo PC ***')

# Creamos una primer orden
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'Bluuetooth')
raton2 = Raton('Gamer', 'Bluuetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', teclado2, raton2, monitor2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('Dell', 'Bluuetooth')
raton3 = Raton('Dell', 'Bluuetooth')
monitor3 = Monitor('Dell', 37)
computadoras3 = Computadora('Dell', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadoras3)
print(orden1)