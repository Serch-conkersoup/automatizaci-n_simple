from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.sanitizar import sanitizar

texto=input("ingrese el texto a sanitizar: ")
resultado= sanitizar(texto)
print ("Texto sanitizado: ", resultado)