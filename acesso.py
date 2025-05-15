from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(options=options)

url = "http://www.7cold.com/glauco"  # <- Substitua pelo seu site real
print(f"Acessando: {url}")
driver.get(url)

sleep(10)  # Espera 10 segundos

print("Fechando navegador")
driver.quit()
