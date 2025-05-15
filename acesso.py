from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(options=options)

driver.get("http://www.7cold.com/glauco")
sleep(10)
driver.quit()
