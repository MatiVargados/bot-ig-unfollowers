# 1. Inputs de texto (<input type="text">)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Buscar el input por su atributo name y escribir texto
input_nombre = driver.find_element(By.NAME, "firstname")
input_nombre.clear()
input_nombre.send_keys("Juan")

input_apellido = driver.find_element(By.NAME, "lastname")
input_apellido.clear()
input_apellido.send_keys("Pérez")


# 2. Botones (<input type="submit"> o <button>)

# Buscar por tipo o texto visible
boton = driver.find_element(By.XPATH, "//button[text()='Submit']")
boton.click()

# O si es un input:
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


#  3. Radio buttons y checkboxes

# Checkbox
checkbox = driver.find_element(By.ID, "vehicle1")
checkbox.click()

# Radio button
radio = driver.find_element(By.ID, "male")
radio.click()


#4. Select (<select>) con Select de Selenium

from selenium.webdriver.support.ui import Select

select_element = Select(driver.find_element(By.ID, "cars"))

select_element.select_by_visible_text("Volvo")
# select_element.select_by_index(0)
# select_element.select_by_value("volvo")

# SE PUEDE PROBAR