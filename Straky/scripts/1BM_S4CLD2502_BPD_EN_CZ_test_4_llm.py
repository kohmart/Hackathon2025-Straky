Zde je skript v Pythonu s využitím Selenium WebDriver, který odpovídá uvedenému testovacímu scénáři:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Krok 1: Log On
try:
    driver.get("URL_SAP_Fiori_launchpad") # nahradit skutečný URL
    print("Log On: SAP Fiori launchpad loaded successfully.")
except Exception as e:
    print("Exception occurred during Log On: ", e)

# Krok 2: Access the App
try:
    app_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "Manage Stock (F1062)")))
    app_element.click()
    print("Access the App: App opened successfully.")
except Exception as e:
    print("Exception occurred during Access the App: ", e)

# Krok 3: Input Material
try:
    material_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "Material Master")))
    plant_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "Plant")))
    material_element.send_keys("RM124")
    plant_element.send_keys("2010")
    plant_element.send_keys(Keys.RETURN)
    print("Input Material: Material entered successfully.")
except Exception as e:
    print("Exception occurred during Input Material: ", e)

# Krok 4: Select Stock
try:
    stock_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "checkboxStock"))) # Nahradit skutečný název prvku
    stock_element.click()
    print("Select Stock: Stock selected successfully.")
except Exception as e:
    print("Exception occurred during Select Stock: ", e)

# Krok 5: Add Initial Entry
try:
    initial_entry_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "Initial Entry")))  # Nahradit skutečný název prvku
    initial_entry_button.click()
    print("Add Initial Entry: Initial entry made successfully.")
    time.sleep(5)  # Pauza pro zobrazení výsledku
except Exception as e:
    print("Exception occurred during Add Initial Entry: ", e)
finally:
    driver.quit()
```
Upozorňuji, že tento skript bude pravděpodobně vyžadovat úpravy pro konkrétní webové stránky SAP Fiori launchpad, například správné označení prvků (`By.NAME`). 

Tento skript provádí několik souběžných operací pro každý krok:
1. Čeká, dokud není prvek připraven k interakci, používá WebDriverWait a očekávané podmínky.
2. Interaguje s prvkem pomocí kliknutí či zadání kláves.
3. Loguje pokrok pomocí příkazu 'print'. Pokud se při některém z kroků objeví výjimka, je tato výjimka zachycena a zaznamenána.