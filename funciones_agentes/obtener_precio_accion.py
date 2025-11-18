# importar la función By de selenium.webdriver.common.by,
# misma que permite seleccionar elementos de una página web
# por medio de selectores CSS.
from selenium.webdriver.common.by import By

# Función para obtener el precio de una acción
# Parámetros:
# - driver: objeto de Selenium WebDriver
# - consulta: cadena de texto que contiene la consulta del usuario
def obtener_precio_accion(driver, consulta):
    # Buscar el precio de una acción en Google
    driver.get(f"https://www.google.com/search?q=precio+acción+{consulta}")

    # Bloque try-except para manejar errores
    try:
        # Obtener el nombre completo de la emprea
        empresa = driver.find_element(By.CSS_SELECTOR, "div[class='PZPZlf ssJ7i B5dxMb']").text

        # Obtener el precio de la acción
        precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text

        # Obtener la divisa de la acción
        divisa = driver.find_element(By.CSS_SELECTOR, "span[jsname='T3Us2d']").text

        # Obtener el ticker de la acción. Éste es el código que se usa para identificar la acción en la bolsa. Por ejemplo, el ticker de Apple es AAPL.
        ticker = driver.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text
        
        return f"{empresa} [{ticker}]  ${precio} {divisa.upper()}."
    except Exception as e:
        return "No se pudo obtener el precio de la acción en este momento."
