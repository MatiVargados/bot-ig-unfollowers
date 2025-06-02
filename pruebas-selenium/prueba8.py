"""
1. Cambiar entre ventanas o pestañas
Cuando hacés clic en algo que abre una nueva pestaña o ventana, Selenium no cambia automáticamente, hay que hacerlo manualmente.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

# Hacer clic en el link que abre una nueva pestaña
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Cambiar a la nueva pestaña
ventanas = driver.window_handles  # Lista de IDs de ventanas abiertas
driver.switch_to.window(ventanas[1])  # Cambia a la segunda pestaña

print("Título nueva pestaña:", driver.title)

driver.close()  # Cierra la pestaña actual

# Volver a la ventana original
driver.switch_to.window(ventanas[0])

driver.quit()

#-----------------------------------------------------------------------------

"""
2. Manejar alertas (pop-ups del navegador)
A veces se abren alertas del navegador (no HTML), como:
alert("¿Estás seguro?");
"""
from selenium.webdriver.common.alert import Alert

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Disparar una alerta
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Cambiar el foco a la alerta
alerta = driver.switch_to.alert
print("Texto de la alerta:", alerta.text)

alerta.accept()  # Aceptar la alerta
# alerta.dismiss()  # Cancelar
# alerta.send_keys("texto")  # Escribir si es una alerta con input

#-----------------------------------------------------------------------------