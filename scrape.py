from selenium import webdriver
from datetime import datetime
import subprocess
import time

url = 'https://www.jps.go.cr/productos/chances'

# Configurar el navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para ejecutar en modo sin cabeza (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Navegar a la página
driver.get(url)

# Esperar 8 segundos antes de obtener el contenido
#time.sleep(8)

# Esperar a que el contenido se cargue completamente (puedes ajustar este tiempo según sea necesario)
driver.implicitly_wait(7)

# Obtener la fecha actual
#fecha_actual = datetime.now().strftime('%A_%d_%B')
# Crear el nombre del archivo con la fecha
#nombre_archivo = f'chances_{fecha_actual}.html'

# Obtener el año actual
ano_actual = datetime.now().year

# Crear el nombre del archivo con la fecha
nombre_archivo = f'{ano_actual}/chances_{datetime.now().strftime("%A_%d_%B")}.html'


# Obtener el contenido HTML después de que se haya ejecutado JavaScript
html_content = driver.page_source

# Cerrar el navegador
driver.quit()

# Guardar el contenido HTML en un archivo con el nombre que incluye la fecha
with open(nombre_archivo, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'Página descargada exitosamente con contenido JavaScript. Guardada como: {nombre_archivo}')

subprocess.run(['python', 'beautifulsoup.py', nombre_archivo])
