"""
EJEMPLO
<input id="usuario" type="text" />
<button id="entrar">Entrar</button>
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tusitio.com")

# ejemplo con DOM (arbol "genealogico" de html)
# el by busca por id 
input_usuario = driver.find_element(By.ID, "usuario")

# para enviar un evento o campo de entrada
input_usuario.send_keys("pepito")

# da la locacion 
boton = driver.find_element(By.ID, "entrar")
boton.click()