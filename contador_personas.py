class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementador el valor del atributo clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estatico')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls): # class
        print('Metodo de clase')
        return cls.contador_personas


if __name__ == '__main__':
    print(("*** Ejemplo contador de objetos ***"))
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()
    # Segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()
    # Tercer objeto
    persona3 = Persona('Juan', 'Kendrick')
    persona3.mostrar_persona()
    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos de personas: {Persona.contador_personas}')
    print(f'Contador objetos de personas (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos de personas (clase): {Persona.get_contador_personas_clase()}')