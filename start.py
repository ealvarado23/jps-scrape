from datetime import datetime
import subprocess

# Obtener el día de la semana actual (0 es lunes, 1 es martes, ..., 6 es domingo)
dia_semana_actual = datetime.now().weekday()

# Verificar si es miércoles (2) o sábado (5)
if dia_semana_actual == 2 or dia_semana_actual == 5:
    # Invocar el script myescript.py
    subprocess.run(['python', 'scrape.py'])
    print("El script se ejecutó porque hoy es miércoles o sábado.")
else:
    print("Hoy no es miércoles ni sábado, el script no se ejecutará.")
