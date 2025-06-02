"""
Esperas en Selenium
Cuando navegás por páginas reales, a veces los elementos no están disponibles inmediatamente, 
y si intentás acceder a ellos antes de que estén listos, tu script lanza errores.
Selenium ofrece dos formas de manejar esto:
"""

# 1. Esperas implícitas
# Es una espera global. Le decís a Selenium: "Esperá hasta X segundos antes de lanzar un error si un elemento no aparece."

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Espera hasta 10 segundos para encontrar elementos

driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")  # Esto esperará si hace falta
search_box.send_keys("Esperas en Selenium")

# Una sola vez al inicio
# Se aplica a todas las búsquedas (find_element y find_elements)

"""
✅ Cuándo usarla:

En proyectos simples o rápidos donde todos los elementos cargan más o menos igual de lento.

Cuando no querés preocuparte demasiado por la sincronización.

Para pruebas personales o scripts internos.

❌ Cuándo evitarla:

En sitios dinámicos o SPA (Single Page Applications como React/Vue), donde algunos elementos cargan con animaciones o AJAX.

Si combinás con esperas explícitas puede haber comportamientos raros, como duplicación de tiempos de espera.
"""

"""-----------------------------------------------------------------------------------------------------------------------------"""

#  2. Esperas explícitas
# Acá le decís a Selenium: "Esperá hasta que aparezca este elemento específico, o que cumpla cierta condición".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))  # Espera solo este elemento

search_box.send_keys("Selenium explicit waits")

"""
Cuando usar cual 
| Situación                          | Tipo de espera recomendada     |
| ---------------------------------- | ------------------------------ |
| Toda la web es lenta               | Implicita (`implicitly_wait`)  |
| Ciertas partes cargan lento        | Explícita (`WebDriverWait`)    |
| Vas a automatizar sitios dinámicos | Explícita + buenas condiciones |
"""

"""
✅ Cuándo usarla:

En sitios dinámicos, donde cada parte de la página puede tardar distinto.

Cuando necesitás interactuar con precisión con formularios, botones o elementos cargados con JavaScript.

Si estás haciendo scraping de datos que aparecen luego de un clic, o al pasar el mouse, etc.

📌 También te permite:

Controlar mejor errores (por ejemplo, dar mensajes si algo no aparece).

Esperar cosas específicas como alertas, cambios de texto, popups, etc.
"""
