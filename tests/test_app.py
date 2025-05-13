from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import subprocess

@pytest.fixture
def driver():
    #iniciar o streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True # Executar o Chrome em modo headless
    driver = webdriver.Chrome(options=options)
    #Iniciar o WebDriver usando GeckoDriverManager
    driver.set_page_load_timeout(10)
    yield driver

    # Finalizar o processo do Streamlit
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Acessar a URL do Streamlit
    driver.get("http://localhost:8501")
    sleep(10)  # Esperar a página carregar
