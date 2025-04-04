Kod v Pythonu, který odpovídá testovacímu scénáři 20 by mohl vypadat následovně:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    # Krok 1
    print("Krok 1: Log On")
    driver.get("http://your-sap-fiori-url")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Logon")))

    # Krok 2
    print("Krok 2: Access the App")
    app = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Confirm-Production-Order-Operation")))
    app.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "PerformWorkScreen")))

    # Krok 3
    print("Krok 3: Enter Production Order and Operation")
    order_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "orderInput")))
    order_input.send_keys("<Production Order Number here>")
    operation_input = driver.find_element_by_id("operationInput")
    operation_input.send_keys("0010")
    enter_button = driver.find_element_by_id("enterButton")
    enter_button.click()

    # Krok 4
    print("Krok 4: Enter Fields in Quantities Section")
    yield_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "yieldInput")))
    yield_input.send_keys("<amount to Confirm>")
    scrap_input = driver.find_element_by_id("scrapInput")
    scrap_input.send_keys("<amount to Scrap>")

    # Krok 5
    print("Krok 5: Check Material Movements")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "MaterialMovementsTable")))

    # Krok 6
    print("Krok 6: Enter Fields in Activities Section")
    setup_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "setupInput")))
    setup_input.send_keys("<setup time>")
    machine_input = driver.find_element_by_id("machineInput")
    machine_input.send_keys("<machine time>")
    labor_input = driver.find_element_by_id("laborInput")
    labor_input.send_keys("<labor time>")

    # Krok 7
    print("Krok 7: Save your entries")
    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "postAndCompleteButton")))
    save_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "confirmationCreated")))

    # Krok 8
    print("Krok 8: Repeat steps")
    driver.get("http://your-sap-fiori-url")

    # Here repeat steps 3 to 7

except Exception as e:
    print("An exception occurred: ", e)

finally:
    driver.quit()
```

Tento skript je nutné upravit podle skutečné implementace vaší webové stránky (URL adresa, ID a CLASS_NAME elementů atd.). Tento kód je psaný pro Firefox, je-li váš prohlížeč jiný, je nutné změnit `webdriver.Firefox()` na `webdriver.Chrome()` pro Chrome nebo na `webdriver.Edge()` pro Edge. Selenuim WebDriver podporuje širokou paletu prohlížečů.