Testovací skript by mohl vypadat následovně:

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Firefox()  # Nebo jiný prohlížeč podle preferencí

def log(message):
    print(message)

try:
    driver.get("http://example.com")  # Nahradit URL stránky, na které se má test provést
    # Krok 1
    try:
        duration_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "duration")))
        if duration_element:
            log("Element Duration nalezen")
        else:
            log("Element Duration nenalezen")
    except TimeoutException:
        log("Element Duration nenalezen - vypršel čas čekání")
    # Krok 2
    try:
        responsibility_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "responsibility")))
        if responsibility_element:
            responsibility_element.send_keys("State the Service Provider, Customer or Joint Service Provider and Customer")
            log("Element Responsibility nalezen a vyplněn")
        else:
            log("Element Responsibility nenalezen")
    except TimeoutException:
        log("Element Responsibility nenalezen - vypršel čas čekání")

except NoSuchElementException as e:
    log(f"Prvek nebyl nalezen: {e}")
finally:
    driver.quit()
```

Tento skript spustí prohlížeč, otevře webovou stránku, najde elementy "Duration" a "Responsibility" a napíše hodnotu do elementu "Responsibility". Pokud některý z prvků nebylo možné najít, vypíše se chybová zpráva. 

Poznámka: ID elementů "duration" a "responsibility" je třeba nahradit skutečnými hodnotami pro danou webovou stránku. Také je nutné nahradit "http://example.com" skutečnou URL dané webové stránky.

Pomocí `WebDriverWait` a `expected_conditions` jsme mohli přidat čekání na elementy. Jakmile je element dostupný, skript pokračuje.

Chybové výpisy jsou zaručeny pomocí try/except bloků a logování je provedeno pomocí funkce `log()`, která vypíše zprávy na konzoli.
