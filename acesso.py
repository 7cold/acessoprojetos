from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configura opções do Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--remote-debugging-port=9222')

# Inicializa o driver do Chrome
driver = webdriver.Chrome(options=options)

# Abre o site
driver.get("https://www.7cold.com")

# Espera o carregamento
time.sleep(2)

# Imprime o título da página
print("Título da página:", driver.title)

# Encerra
driver.quit()
