from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

empresa=input ("escribe la empresa: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get(f"https://www.google.com/search?q=accion+de+{empresa}")
sleep(40)
