from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ejemplo.com")  # Reemplazá por la URL real

#-----------------------------------------------------------------------

driver.back()       # Ir a la página anterior
driver.forward()    # Ir a la siguiente
driver.refresh()    # Recargar la página actual

#-----------------------------------------------------------------------

# Abrir una nueva pestaña
driver.execute_script("window.open('https://otraweb.com', '_blank');")

# Cambiar a esa nueva pestaña
driver.switch_to.window(driver.window_handles[1])  # [0] es la original

#-----------------------------------------------------------------------

driver.switch_to.window(driver.window_handles[0])  # Volver a la original

#-----------------------------------------------------------------------    

driver.close()  # Cierra la pestaña activa

#⚠️ Después de cerrarla, deberías volver a cambiar el foco a una pestaña activa:

driver.switch_to.window(driver.window_handles[0])

#-----------------------------------------------------------------------

from selenium.webdriver.common.alert import Alert

alerta = Alert(driver)
print(alerta.text)    # Leer el texto
alerta.accept()       # Hacer clic en "Aceptar"
alerta.dismiss()    # Hacer clic en "Cancelar"
alerta.send_keys("Texto")  # Escribir en el input si es una alerta con input

#-----------------------------------------------------------------------


"""
EJEMPLO

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Abrir nueva pestaña con otra página
driver.execute_script("window.open('https://example.com', '_blank');")
time.sleep(2)

# Cambiar a la segunda pestaña
driver.switch_to.window(driver.window_handles[1])
print("Estamos en:", driver.title)

# Cerrar pestaña actual y volver a la primera
driver.close()
driver.switch_to.window(driver.window_handles[0])
print("Volvimos a:", driver.title)

driver.quit()
"""