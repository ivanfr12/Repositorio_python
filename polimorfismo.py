from herencias_python import animal1, gato1


class Animal:
    def hacer_sonido(self):
        print('Hago un pitido...')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

print('*** Ejemplo Polimorfismo ***')
print('Clase padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()

# Definimos un objeto de la clase perro
print('\nClase hija perro: ')
perro1 = Perro()
perro1.hacer_sonido() # Polimorfismo (se manda a llamar el metodo segun el objeto que se esta ejecutando)

# clase Gato
print('\nClase hija gato: ')
gato1 = Gato()
gato1.hacer_sonido()

