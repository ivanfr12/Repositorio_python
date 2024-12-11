from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa
print("*** Sistema de Empleados ***")

# Crear una instancia de una empresa
empresa1 = Empresa('Mi Empresa')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Pedro', 'Informatica')
empresa1.contratar_empleado('Joan', 'Marketing')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

# Obtener el numero total de empleados de la empresa creada
print(f'Total de empleados en la empresa: {Empleado.obtener_total_empleados()}')

# Obetener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')
print(f'Empleados en el departamento de Informatica: {empresa1.obtener_numero_empleados_departamento('Informatica')}')
print(f'Empleados en el departamento de Marketing: {empresa1.obtener_numero_empleados_departamento('Marketing')}')
print(f'Empleados en el departamento de Recursos Humanos: {empresa1.obtener_numero_empleados_departamento('Recursos Humanos')}')

# Mostrar todos los empleados de la empresa
empresa1.mostrar_todos_empleados()