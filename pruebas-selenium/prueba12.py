from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

# Click para disparar una alerta
driver.find_element(By.ID, "alertexamples").click()

# Esperar y aceptar la alerta
time.sleep(1)
Alert(driver).accept()

driver.quit()

"""
Manejo de alertas, pop-ups y ventanas nuevas
Estas situaciones son comunes en formularios, sistemas bancarios, sitios con confirmaciones, etc.
"""

"""
1. Aceptar una alerta simple
Las alertas de JavaScript bloquean el flujo hasta que se aceptan o cierran.
"""
from selenium.webdriver.common.alert import Alert

alerta = Alert(driver)
alerta.accept()  # hace clic en "Aceptar"

"""
2. Cancelar una alerta (si tiene opción)
Algunas alertas tienen botón “Cancelar” (como confirm() en JS):
"""
alerta.dismiss()  # hace clic en "Cancelar"

"""
3. Leer el texto de una alerta
"""
print(alerta.text)

"""
4. Escribir en un prompt
Algunas alertas permiten ingresar texto (prompt() en JS):
"""
alerta.send_keys("Texto de prueba")
alerta.accept()

"""
5. Manejo de múltiples ventanas o pestañas
Cuando hacés clic en un link que abre una nueva ventana/pestaña:
"""

# Guardar ventana actual
main_window = driver.current_window_handle

# Click que abre nueva ventana
driver.find_element(By.LINK_TEXT, "Abrir").click()

# Obtener todas las ventanas abiertas
ventanas = driver.window_handles

# Cambiarse a la nueva ventana
for v in ventanas:
    if v != main_window:
        driver.switch_to.window(v)
        break

# Ahora estás en la nueva ventana
print(driver.title)

# Volver a la principal
driver.switch_to.window(main_window)


"""
| Función / operador | Ejemplo                         | Significado                        |
| ------------------ | ------------------------------- | ---------------------------------- |
| `//`               | `//div`                         | Busca en cualquier nivel           |
| `.`                | `.//a`                          | Desde el nodo actual               |
| `@atributo`        | `@class`, `@href`, `@role`      | Accede a atributos                 |
| `contains()`       | `contains(@class, "btn")`       | Si un atributo contiene una cadena |
| `text()`           | `//button[text()="Aceptar"]`    | Busca por texto exacto             |
| `starts-with()`    | `starts-with(@id, "user")`      | Comienza con...                    |
| `and / or`         | `@role="dialog" and @class="x"` | Combinación de condiciones         |

"""