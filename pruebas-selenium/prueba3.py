"""
EJEMPLO
<input type="text" id="usuario" />
<button id="enviar">Entrar</button>
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://ejemplo.com")  # Reemplazá por la URL real

# Encontrar el input y escribir
input_usuario = driver.find_element(By.ID, "usuario")
input_usuario.send_keys("pepito123")

# Esperar 5 segundos para ver lo que pasa
time.sleep(5)

# Hacer clic en el botón
boton = driver.find_element(By.ID, "enviar")
boton.click()

"""
<input class="form-control" name="email" />
"""
# Por clase
driver.find_element(By.CLASS_NAME, "form-control").send_keys("correo@mail.com")

# Por nombre
driver.find_element(By.NAME, "email").send_keys("correo@mail.com")

# Por tag
todos_los_inputs = driver.find_elements(By.TAG_NAME, "input")

"""
<button>Ingresar</button>
"""
# Busca cualquier botón con ese texto
boton = driver.find_element(By.XPATH, "//button[text()='Ingresar']")
boton.click()

"""
<div class="card">
  <button class="btn">Ver más</button>
</div>
"""
# CSS: dentro de un div.card, buscá un botón.btn
boton = driver.find_element(By.CSS_SELECTOR, "div.card > button.btn")
boton.click()