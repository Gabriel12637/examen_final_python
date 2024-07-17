"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
# Definición del diccionario con dos registros de un alumno
alumnos = {
    1: {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"},
    2: {"nombre": "María", "edad": 22, "carrera": "Medicina"}
}

# Función para imprimir los registros de los alumnos
def imprimir_registros():
    for id_alumno, datos in alumnos.items():
        print(f"ID: {id_alumno}, Nombre: {datos['nombre']}, Edad: {datos['edad']}, Carrera: {datos['carrera']}")

# Función para editar un campo específico de un registro
def editar_registro(id_alumno, campo, nuevo_valor):
    if id_alumno in alumnos:
        alumnos[id_alumno][campo] = nuevo_valor
        print("Registro actualizado correctamente.")
    else:
        print("ID de alumno no encontrado.")

# Probando las funciones
print("Registros actuales:")
imprimir_registros()

# Editar el registro con ID 1, cambiando la edad
editar_registro(1, "edad", 21)

# Imprimir los registros actualizados
print("\nRegistros actualizados:")
imprimir_registros()
