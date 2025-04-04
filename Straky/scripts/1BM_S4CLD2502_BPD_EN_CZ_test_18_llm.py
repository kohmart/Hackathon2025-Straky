Níže je příklad jak může vypadat Selenium testovací skript na základě dodaného testovacího scénáře. Skript je napsán v programovacím jazyce Python:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Krok 1: Log On
print("Krok 1: Log On")
try:
    driver.get('http://your-url.com')  # Doplnit URL aplikace
    # log_on_button by mělo být ID tlačítka pro Log On
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'log_on_button'))).click()
except Exception as e:
    print(str(e))

# Krok 2: Access the App
print("Krok 2: Access the App")
try:
    # co02_button by mělo být ID tlačítka pro otevření Change Production Order (CO02)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'co02_button'))).click()
except Exception as e:
    print(str(e))

# Krok 3: Enter Production Order Data
print("Krok 3: Enter Production Order Data")
try:
    # production_order_input by mělo být ID textového pole pro zadání čísla výrobní objednávky
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'production_order_input'))).send_keys('order_number')
    # continue_button by mělo být ID tlačítka pro pokračování
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'continue_button'))).click()
except Exception as e:
    print(str(e))

# Krok 4: Navigate to Output Management
print("Krok 4: Navigate to Output Management")
try:
    # output_management_button by mělo být ID tlačítka pro navigaci do Output Management
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'output_management_button'))).click()
except Exception as e:
    print(str(e))

# Aplikace může mít více kroků, které mohou být podobné výše uvedeným  
          
driver.quit()
```

Prosím poznamenejte, že pro konkrétní použití je třeba doplnit správné selectory / identifikátory prvků formulářů (ID, jméno, CSS, atd.) a správné URL aplikace. Jmena tlačítek a textových polí jsou pouze ilustrativní a ve skutečnosti budou pravděpodobně odlišná.