# 1. Crear una lista vacía llamada calificaciones
calificaciones = []

# 2. Solicitar al usuario que cargue los 10 valores
print("Por favor, ingresá las 10 calificaciones:")
for i in range(10):
    nota = float(input(f"Ingresá la calificación {i + 1}: "))
    calificaciones.append(nota)

# 3. Calcular la suma de todos los valores usando sum()
suma_total = sum(calificaciones)

# 4. Mostrar el resultado
print("\n--- Resultados ---")
print("Lista de calificaciones ingresadas:", calificaciones)
print("La suma de todas las calificaciones es:", suma_total)