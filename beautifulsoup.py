from datetime import datetime
from bs4 import BeautifulSoup
import subprocess

# Obtener el nombre del archivo
nombre_archivo = f'2024/chances_{datetime.now().strftime("%A_%d_%B")}.html'

# Cargar el contenido HTML desde el archivo descargado
with open(nombre_archivo, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todas las etiquetas 
parrafos = soup.find_all('span', class_=lambda x: x and ('numero' in x or 'serie' in x and '_0' in x))

# Imprimir el texto de cada párrafo 
for parrafo in parrafos:
    print(parrafo.text)

# Abrir el archivo 'lucky.txt' en modo append
with open('lucky.txt', 'a', encoding='utf-8') as lucky_file:
    # Imprimir el texto de cada párrafo y escribirlo en el archivo
    for parrafo in parrafos:
        texto_parrafo = parrafo.text
        print(texto_parrafo)
        lucky_file.write(texto_parrafo + '\n')

subprocess.run(['python', 'sort.py', nombre_archivo])

