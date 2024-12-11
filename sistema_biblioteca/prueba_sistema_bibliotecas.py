# Creamos un objeto de tipo biblioteca
from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

bibliotecaMexico = Biblioteca('Biblioteca Mexico')

# Agregamos libros
libro1 = Libro('El Alquimista', 'Paulo Cohelo', 'Ficcion')
libro2 = Libro('1994', 'George Orwell', 'Ficcion')
libro3 = Libro('El codigo Da Vinci', 'Dan Brown', 'Misterio')
libro4 = Libro('Rayuela', 'Julio Cortazar', 'Novela')
libro5 = Libro('Veronica decide morir', 'Paulo Cohelo', 'Ficcion')

# Agregar los libros a la biblioteca
bibliotecaMexico.agregar_libros(libro1)
bibliotecaMexico.agregar_libros(libro2)
bibliotecaMexico.agregar_libros(libro3)
bibliotecaMexico.agregar_libros(libro4)
bibliotecaMexico.agregar_libros(libro5)

# NOmbre de la biblioteca
print(f'*** Bienvenidos a la {bibliotecaMexico.nombre} ***')

# Buscar libros por autor
print(f'\nLibros de Paulo Cohelo: ')
bibliotecaMexico.buscar_libros_por_autor('Paulo Cohelo')

# Buscar libros por genero
print(f'\n Libros de ficcion: ')
bibliotecaMexico.buscar_libros_por_genero('Ficcion')

# Mostrar todos los libros de la biblioteca
bibliotecaMexico.mostrar_todos_los_libros()