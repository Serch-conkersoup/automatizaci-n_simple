from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion

from utils.sanitizar import sanitizar

options = Options()
options.add_argument("--headless=chrome")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return "clima"
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return "precio"
    return None


print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")

while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)

    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
        continue

    # Llamar a la función correcta
    if funcion_agente == "clima":
        resultado = obtener_clima(driver, user_input)
    elif funcion_agente == "precio":
        resultado = obtener_precio_accion(driver, user_input)

    print(f">>> {resultado}")
    
