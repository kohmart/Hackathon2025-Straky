```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Vybere a nastartuje prohlizec
driver = webdriver.Chrome()

# Otevře webovou stránku
driver.get("http://your-website.com")

# Čas pro načtení stránky
time.sleep(5)

# Připraví hodnotu pro vyhledávání elementu
value = "<State the Service Provider, Customer or Joint Service Provider and Customer>"

try:
    # Vyhledá element 'Duration' na stránce a nastaví hodnotu
    duration_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Duration"))
    )
    duration_element.clear()
    print("Element 'Duration' byl nalezen.")

except TimeoutException:
    print("Element 'Duration' nebyl nalezen.")
except Exception as e:
    print(f"Doslo k chybe: {e}")

try:
    # Vyhledá element 'Responsibility' na stránce a nastaví hodnotu
    responsibility_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Responsibility"))
    )
    responsibility_element.clear()
    responsibility_element.send_keys(value)
    print("Element 'Responsibility' byl nalezen a nastaven hodnotou.")

except TimeoutException:
    print("Element 'Responsibility' nebyl nalezen.")
except Exception as e:
    print(f"Doslo k chybe: {e}")

# Zavře prohlizec
driver.quit()
```

V tomto skriptu měníme hodnoty elementů 'Duration' a 'Responsibility' na webových stránkách. Používáme Selenium a WebDriver pro ovládání prohlížeče a vyhledávání elementů. Pro čekání na načítání elementů používáme WebDriverWait a ošetřujeme výjimky pro případ, že element není nalezen nebo dojde k jiné chybě.