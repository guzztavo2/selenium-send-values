from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By

def select_element(driver, select, by):
    try:
        element = driver.find_element(by, select)
        return element
    except exceptions.NoSuchElementException:
        return False
    except Exception as e:
        print(f"Erro não identificado: {e}")
        return False

def send_keys_to_element(driver, select, value, by):
    element = select_element(driver, select, by)
  
    if element is False:
        raise exceptions.NoSuchElementException(f"Elemento não encontrado {select} - {by}")
      
    try:
        if element.get_attribute("value") == value:
            driver.execute_script(f"arguments[0].blur();", element)
            return True
        driver.execute_script(f"arguments[0].value = '{value}';", element)        
    except (exceptions.StaleElementReferenceException, exceptions.InvalidElementStateException):
        try:
            driver.execute_script(f"arguments[0].value = '{value}';", select_element(driver, select, by))
        except:
            raise exceptions.NoSuchElementException(f"Elemento não encontrado {select} - {by}")
    return True

def initScreen():
    options = webdriver.ChromeOptions()
    options.add_argument("-disable-quic")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(f'user-agent=Mozilla/5.0')

    driver = webdriver.Chrome(options=options)
    
    driver.get("url to get")
    driver.implicitly_wait(30)
    return driver

driver = initScreen()
send_keys_to_element(driver, "body > input", By.CSS_SELECTOR, "TESTE 123")
