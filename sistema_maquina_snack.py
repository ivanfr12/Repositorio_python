# Sistema de maquina de snack

print('--- Maquina de Snacks ---')

# Definicion de la lista de snacks

snack = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). son los snack que queremos comprar
productos = []

# Falta agregar las funciones de la maquina snacks

def mostrar_snack():
    print('--- Snacks disponibles ----')
    for snacks in snack:
        print(f'\tId: {snacks.get('id')} -> {snacks.get('nombre')} - '
              f'${snacks.get('precio')}')


def buscar_snack_por_id(id_a_buscar):
    for snacks in snack:
        if snacks.get('id') == id_a_buscar:
            return snacks
    # Si llegamos al final y no encontramos el snack regresa none
    return None

def comprar_snack():
    id_snack = int(input('Que snack quieres comprar (id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack no encontrado por id: {snack_encontrado}')



def mostrar_ticket():
    ticket = f'\t--- Ticket de venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.get('nombre')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)



# Programa principal
if __name__ == '__main__':
    print('*** Maquina de Snack ***')
    # Creamos el menu
    while True:
        print(f'''Menu:
        1. Mostrar Snack
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snack()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('!Gracias por usar nuestro programa, hasta pronto¡')
            break
        else:
            print('Opcion invalida, selecciona otra opcion.')


