from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Caminho do driver padrão no GitHub Actions
driver = webdriver.Chrome(options=options)

url = "https://www.7cold.com/glauco"  # Substitua aqui
print(f"Acessando: {url}")
driver.get(url)

sleep(10)

print("Fechando navegador")
driver.quit()
