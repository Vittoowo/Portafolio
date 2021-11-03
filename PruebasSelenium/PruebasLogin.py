from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path="./PruebasSelenium/geckodriver.exe")

driver.get("http://127.0.0.1:8000/")
time.sleep(3)

#Tienes que mandarle la direccion completa del archivo
#con Firefox presenta problemas ya que no reconoce el archivo

driver.find_element_by_name("login").click()
