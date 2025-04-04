Následující je příklad Selenium testovacího skriptu v Pythonu:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Krok 1: Log on
print("Krok 1: Log On")
driver.get("url to SAP Fiori launchpad")
assert "SAP Fiori launchpad" in driver.title
print("Úspěšně přihlášen.")

# Krok 2: Access the App
print("Krok 2: Access the App")
driver.get("url to Monitor Material Coverage")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MonitorMaterialCoverage")))
    print("Aplikace je načtena.")
except Exception as e:
    print("Chyba při načítání aplikace: ", e)

# Krok 3: Check Default Settings
print("Krok 3: Check Default Settings")
try:
    user_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserIcon")))
    user_icon.click()
    app_settings = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "AppSettings")))
    app_settings.click()
    print("Nastavení aplikace bylo úspěšně otevřeno.")
except Exception as e:
    print("Chyba při kontrole nastavení: ", e)

# Krok 4: Select Material
print("Krok 4: Select Material")
try:
    material_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MaterialField")))
    material_field.send_keys("SG224")
    go_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "GoButton")))
    go_button.click()
    print("Materiál byl vybrán.")
except Exception as e:
    print("Chyba při výběru materiálu: ", e)

# Krok 5: Find Planned Order
print("Krok 5: Find Planned Order")
try:
    order_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "OrderInfo")))
    print("Plánovaná objednávka byla nalezena.")
except Exception as e:
    print("Chyba při hledání plánované objednávky: ", e)

# Krok 6: Convert Planned Order to Production Order
print("Krok 6: Convert Planned Order to Production Order")
try:
    action_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ActionDropdown")))
    action_dropdown.click()
    convert_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ConvertToProductionOrder")))
    convert_option.click()
    convert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ConvertButton")))
    convert_button.click()
    print("Plánovaná objednávka byla převedena na výrobní objednávku.")
except Exception as e:
    print("Chyba při převodu plánované objednávky na výrobní objednávku: ", e)

driver.quit()
```
Upozorňujeme, že tento kód je vzorový a nebude fungovat bez upravení podle konkrétní SAP Fiori aplikace (je třeba nahradit "url to SAP Fiori launchpad" pravou URL, rovněž ID elementů jsou uvedeny náhodně). Zároveň je doporučeno používat správné ovladače vzhledem k prohlížeči (v tomto případě je použit ovladač pro Firefox).