class Animal:

    def comer(self):
        print('Como muchas veces al dia')


    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescribiendo el metodo heredado de la clase padre
    def dormir(self):
        print('Duermo 15 horas al dia')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo hacer miau')

    def dormir(self):
        print('De noche no duermo')


# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase padre, soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() # Se llama el motodo sobreescrito de la clase hija
perro1.hacer_sonido()

print('\n Clase hija, soy un gato')
gato1 = Gato()
gato1.comer()
gato1.dormir()
gato1.hacer_sonido()