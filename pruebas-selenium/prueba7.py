from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Hacer clic en el botón que carga el contenido
driver.find_element(By.CSS_SELECTOR, "#start button").click()

# Esperar hasta que el texto aparezca
wait = WebDriverWait(driver, 10)
mensaje = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

print("Texto cargado:", mensaje.text)  # Debe imprimir "Hello World!"

driver.quit()

#-------------------------------------------------------------------------

"""
1- Importar lo necesario

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""

# 2. Esperar a que un elemento esté visible

wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos
elemento = wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
elemento.click()

"""
3. Otras condiciones útiles
+-------------------------------------------+-----------------------+
+ Condición Selenium                        | ¿Qué hace?            |
+ presence_of_element_located               | Existe en el DOM      |
+ visibility_of_element_located             | Visible (lo podés ver)|
+ element_to_be_clickable                   | Se puede hacer clic   |
+ text_to_be_present_in_element             | Espera cierto texto   |
+ frame_to_be_available_and_switch_to_it    | Espera un iframe      |
+-------------------------------------------+-----------------------+
""" 

wait.until(EC.element_to_be_clickable((By.NAME, "enviar"))).click()