from catalogo_peliculas.servicio_peliculas import ServicioPeliculas
from catalogo_peliculas.pelicula import Pelicula


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()


    def mostrar_menu(self):
        print('*** App Catalogo Peliculas ***')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar pelicula
                2. Listar peliculas
                3. Eliminar catalogo de peliculas
                4. Salir''')
                opcion = int(input("Escribe tu opcion (1-4): "))
                if opcion == 1:
                    nombre_pelicula = input('Dame el nombre de la pelicula: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print("Salimos del programa...")
                    break
                else:
                    print("Opcion invalida, Introduce un valor entre 1 y 4.")

            except ValueError:
                print('Error: introduce un numero valido.')
            except Exception as e:
                print(f'Ocurrio un error: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()