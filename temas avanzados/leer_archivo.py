print('-- Leer archivo con Python --')

nombre_archivo = 'mi_archivo.txt'

# Leer un archivo usando el metodo readlineas
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las lineas del archivo
    print(archivo.readline())
    lineas = archivo.readline()
    for linea in lineas:
        print(linea.strip())

# Leer todo el contenido del archivo usando read
print('Leyendo el contenido con el metodo read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())