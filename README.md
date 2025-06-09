# bot-ig-unfollowers

## ⚠️ Aviso Legal
Este proyecto es únicamente con fines **educativos y personales**.
El uso de Selenium sobre sitios como Instagram puede ir en contra de sus **Términos de Servicio**. No se recomienda usar este código para scraping automatizado en cuentas ajenas o con fines comerciales.
Este proyecto no recolecta ni almacena datos de terceros. Funciona solo con la cuenta del usuario autenticado.

## 📌 Descripción
Este bot automatiza el proceso de comparar seguidores y seguidos en Instagram utilizando Selenium.

## 🚀 Funcionalidades
- Exportar lista de seguidores y seguidos
- Comparar listas y detectar quién no te sigue
- Automatización parcial con Selenium (ver detalles abajo)

## ⚙️ Requisitos
- Python 3.13
- Google Chrome
- WebDriver de Chrome (chromedriver)
- Selenium

## 🤖 Automatización
El código actualmente es **95% automático**. Selenium se encarga de iniciar sesión pero si llegas a tener la **verificacion en dos pasos** tenes que poner manualmente el codigo y darle al boton aceptar para que el programa pueda abrir las listas de seguidores y seguidos, y comenzar a extraer los datos.
Sin embargo, **no se ha logrado automatizar el scroll completo** en el cuadro emergente de seguidores/seguidos.  
Cuando veas que el cuadro tiene un **recuadro rojo**, deberás **bajar manualmente el scroll hasta que se carguen todos los usuarios**.
Una vez hecho eso, el script continúa automáticamente.
