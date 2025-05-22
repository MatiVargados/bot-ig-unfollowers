from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ejemplo.com")  # Reemplazá por la URL real

# Esperar hasta que el botón esté "clickeable" (máximo 10 segundos)
wait = WebDriverWait(driver, 10)

boton = wait.until(EC.element_to_be_clickable((By.ID, "enviar")))

boton.click()

"""
Principales condiciones de espera (expected_conditions):
- presence_of_element_located → está en el DOM
- visibility_of_element_located → es visible
- element_to_be_clickable → se puede hacer clic
- text_to_be_present_in_element → aparece un texto
"""

driver.implicitly_wait(5)  # Espera implícita de hasta 5 segundos
# No es la más recomendada para proyectos grandes porque espera igual para todo, aunque no siempre haga falta.


# EJEMPLOS --------------------------------------------------------------------

# Esperar a que el input esté presente y escribir
input_usuario = wait.until(EC.presence_of_element_located((By.ID, "usuario")))
input_usuario.send_keys("miusuario")

# Esperar a que el botón sea clickeable
boton = wait.until(EC.element_to_be_clickable((By.ID, "enviar")))
boton.click()

# -----------------------------------------------------------------------------
