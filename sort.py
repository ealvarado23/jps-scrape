from collections import Counter

# Leer el contenido del archivo 'lucky.txt'
with open('lucky.txt', 'r', encoding='utf-8') as lucky_file:
    # Leer todas las líneas del archivo y combinarlas en un solo string
    contenido = lucky_file.read()

# Separar el string en líneas y crear una lista de números
numeros = [int(linea.strip()) for linea in contenido.split('\n') if linea.strip()]

# Usar Counter para contar la frecuencia de cada número
frecuencia_numeros = Counter(numeros)

# Ordenar los números por frecuencia de mayor a menor
numeros_ordenados = sorted(frecuencia_numeros.items(), key=lambda x: x[1], reverse=True)

# Imprimir los números ordenados
for numero, frecuencia in numeros_ordenados:
    print(f'Número: {numero}, Frecuencia: {frecuencia}')

# Guardar los números ordenados en un archivo llamado 'lucky_SORTED.txt'
with open('lucky_SORTED.txt', 'w', encoding='utf-8') as sorted_file:
    for numero, frecuencia in numeros_ordenados:
        linea = f'Número: {numero}, Frecuencia: {frecuencia}\n'
        sorted_file.write(linea)
