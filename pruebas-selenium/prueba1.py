from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Abre Chrome con Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# Imprime el título de la página
print(driver.title)

# Cierra el navegador
driver.quit()