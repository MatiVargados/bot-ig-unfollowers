from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Simular rellenado (si los inputs existieran en esa página)
driver.find_element(By.ID, "fname").send_keys("Juan")
driver.find_element(By.ID, "lname").send_keys("Pérez")

# Checkboxes (esto es solo si existieran en la página)
checkbox = driver.find_element(By.ID, "suscribir")
checkbox.click()

# Radios
radio = driver.find_element(By.ID, "masculino")
radio.click()

# Select dropdown (si existiera)
dropdown = Select(driver.find_element(By.ID, "pais"))
dropdown.select_by_visible_text("Argentina")

# Simular envío
driver.find_element(By.ID, "enviar").click()

time.sleep(3)
driver.quit()

#---------------------------------------------------------------------

# 1. Rellenar un formulario básico
# (By.NAME, By.ID, By.CLASS_NAME, etc., dependen del atributo HTML del input)

driver.find_element(By.NAME, "username").send_keys("tu_usuario")
driver.find_element(By.NAME, "password").send_keys("tu_contraseña")
driver.find_element(By.NAME, "submit").click()

# 2. Checkboxes y botones de radio

checkbox = driver.find_element(By.ID, "acepto")
if not checkbox.is_selected():
    checkbox.click()

radio = driver.find_element(By.ID, "opcion1")
radio.click()

# 3. Selects (menú desplegable)

from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "pais"))
dropdown.select_by_visible_text("Argentina")


# También podés usar:
# dropdown.select_by_value("ar")
# dropdown.select_by_index(3)