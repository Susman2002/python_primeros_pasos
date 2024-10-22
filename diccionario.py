# Crear un diccionario
mi_diccionario = {
    "nombre": "Alejandro",
    "edad": 22,
    "ciudad": "La Paz"
}

# Acceder a un valor usando su clave
print(mi_diccionario["nombre"])  # Salida: Alejandro

# Modificar un valor
mi_diccionario["edad"] = 23

# Añadir un nuevo par clave-valor
mi_diccionario["profesion"] = "Estudiante de Informática"

# Eliminar un elemento por su clave
del mi_diccionario["ciudad"]

# Recorrer un diccionario
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")


