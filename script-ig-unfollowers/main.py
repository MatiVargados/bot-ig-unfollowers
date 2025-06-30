from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

usuario = ""
contrasenia = ""

# Se almacena el servicio de chrome 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(3)

# abre una pestaña chrome (en este caso instagram)
link = "https://www.instagram.com/"
driver.get(link)
time.sleep(random.uniform(1.5, 3))

# el by busca por lo que le pidas (id, xpath, link_text, name, tag_name, class_name o css_selector)
# find_element devuelve un elemento web
box_usuario = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")
box_usuario.send_keys(usuario)
time.sleep(random.uniform(1.5, 3))

box_contrasenia = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input")
box_contrasenia.send_keys(contrasenia)
time.sleep(random.uniform(1.5, 3))

# oprime el boton para entrar a la cuenta
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button").click()

print("YA SE INICIO SESION")

# Esperar 30 segundos (para ver si tiene que poner la verificacion de 2 pasos)
time.sleep(30)

link += usuario + "/"

driver.get(link)
time.sleep(random.uniform(4.5, 6.5))

time.sleep(1)
cantidad_seguidores = int(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span/span").text.replace(',', ''))

# Click en "seguidores"
seguidores_link = driver.find_element(By.PARTIAL_LINK_TEXT, "seguidores")
seguidores_link.click()
time.sleep(4)

def dar_usuarios(cantidad_usuarios) -> list[str]:
    #scroll_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//div[@style="height: auto; overflow: hidden auto;"]')))
    
    scroll_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//div[contains(@style, "overflow: hidden auto")]'))
    )

    # Borde rojo para confirmar visualmente que se puede arrancar a manipular (es decir, bajar el scroll)
    driver.execute_script("arguments[0].style.border='2px solid red'", scroll_box)
    
    print("BAJA EL SCROLL PARA PODER CARGAR TODOS LOS USUARIOS")

    cantidad_usuarios_cargada = 0
    iteracion = 0

    while cantidad_usuarios > cantidad_usuarios_cargada:
        driver.execute_script("arguments[0].scrollTop += 200", scroll_box)
        time.sleep(1)
        cantidad_usuarios_cargada = len(driver.find_elements(By.CLASS_NAME, '_ap3a._aaco._aacw._aacx._aad7._aade'))

        #cuando llegue a los ultimos 5% de todos tus seguidores (por si hay cuentas muertas [usualmente las cuentas muertas son - del 5% de cantidad de cuentas totales])
        cinco_porciento_restante = cantidad_usuarios - (cantidad_usuarios * 0.05)
        if cinco_porciento_restante < cantidad_usuarios_cargada:
                # luego de que se sepa que estan en el 5 % de tus seguidores iterara unas ultimas 10 veces 
                # para que te deje cargar los usuarios que faltan y en caso de que si existan usuarios muertos rompa el bucle
                # (!solo para cuentas grandes! en caso de que el programa se corte antes de lo debido subanle de 10 hasta lo q necesiten)
                if iteracion > 10: # <--- (este numero debes aumentar si tu cuenta es muy grande)
                    break

                iteracion += 1                 

        print(f"{cantidad_usuarios} / {cantidad_usuarios_cargada}")

    # Dar usuarios
    get_usuarios = driver.find_elements(By.CLASS_NAME, '_ap3a._aaco._aacw._aacx._aad7._aade')

    lista_usuarios = []

    for i in get_usuarios:
        usuario = i.text
        lista_usuarios.append(usuario) 

    return lista_usuarios

lista_seguidores = dar_usuarios(cantidad_seguidores)

# Recargo la pagina para evitar errores
driver.get(link)
time.sleep(random.uniform(4.5, 6.5))

time.sleep(1)
cantidad_seguidos = int(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span/span").text.replace(',', ''))

# Click en seguidos
seguidos_link = driver.find_element(By.PARTIAL_LINK_TEXT, "seguidos")
seguidos_link.click()
time.sleep(4)

lista_seguidos = dar_usuarios(cantidad_seguidos)

#----------------------#
# COMPARADOR DE LISTAS #

lista_no_me_siguen = []

for i in range(len(lista_seguidos)):
    encontrado = False
    for j in range(len(lista_seguidores)):
        if lista_seguidos[i] == lista_seguidores[j]:
            encontrado = True
            break

    if encontrado == False:
        lista_no_me_siguen.append(lista_seguidos[i])

for usuario in lista_no_me_siguen:
    print("-----------------------------------")
    print(usuario)
print("-----------------------------------")

cantidad_usua_sin_seguirme = len(lista_no_me_siguen)
print(f"No te siguen: {cantidad_usua_sin_seguirme} usuarios")
