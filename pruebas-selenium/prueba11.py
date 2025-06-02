from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Screenshot de toda la página
driver.save_screenshot("pantalla_completa.png")

# Buscar y capturar un elemento
elemento = driver.find_element(By.TAG_NAME, "h1")
elemento.screenshot("titulo.png")

# Scroll hasta el pie de página
footer = driver.find_element(By.TAG_NAME, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", footer)

# Scroll hasta abajo de todo
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.quit()

"""-------------------------------------------------------------------------------------"""

# CAPTURA DE PANTALLA

driver.save_screenshot("pantalla_completa.png")

# CAPTURAR UN ELEMENTO EN ESEPCIFICO

elemento = driver.find_element(By.ID, "logo")
elemento.screenshot("logo.png")
"""
🔹 Captura solo el área de la pantalla donde está ese elemento.
🧠 Útil para validar visualmente si un botón, imagen o banner se cargó correctamente.
"""

# Hacer scroll hasta un elemento
# (A veces necesitás bajar el scroll para ver o interactuar con algo)
from selenium.webdriver.common.action_chains import ActionChains

elemento = driver.find_element(By.ID, "piePagina")
actions = ActionChains(driver)
actions.move_to_element(elemento).perform()

# O una versión más directa con JavaScript:
driver.execute_script("arguments[0].scrollIntoView(true);", elemento)


#Hacer scroll hacia abajo en la página completa
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")