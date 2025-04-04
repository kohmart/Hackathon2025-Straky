Následuje ukázka, jak by mohl vypadat Python selenium skript na základě výše uvedeného scenáře:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

# Zadejte cestu k ovladači chrome
webdriver_service = Service('C:/path/to/chromedriver')

# Inicializace webdriver
driver = webdriver.Chrome(service=webdriver_service)
driver.get('http://www.example.com')  # Nahraďte 'http://www.example.com' adresou stránky, kterou chcete otestovat

# Krok 1: Vyplnění pole Duration
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'duration')))
    driver.find_element_by_id('duration').clear()
    print('Element Duration nalezen a vyčištěn')
except TimeoutException:
    print('Element Duration nebyl nalezen do 10 vteřin')
except NoSuchElementException:
    print('Element Duration neexistuje')

# Krok 2: Vyplnění pole Responsibility
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'responsibility')))
    responsibility_element = driver.find_element_by_id('responsibility')
    responsibility_element.clear()
    responsibility_element.send_keys('<State the Service Provider, Customer or Joint Service Provider and Customer>')
    print('Element Responsibility nalezen, čištěn a vyplněn')
except TimeoutException:
    print('Element Responsibility nebyl nalezen do 10 vteřin')
except NoSuchElementException:
    print('Element Responsibility neexistuje')

# Uzavření ovladače
driver.quit()
```

Poznámka: Nezapomeňte nahradit `'C:/path/to/chromedriver'` skutečnou cestou k umístění ovladače Chrome na vašem počítači a `'http://www.example.com'` skutečnou URL webu, který chcete testovat. Také ID elementů "duration" a "responsibility" musí odpovídat ID elementů na webu. Tento kód předpokládá, že ID elementů jsou "duration" a "responsibility", což nemusí nutně odpovídat vaší webové stránce.