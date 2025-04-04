Následuje ukázkový selenium testovací skript v Pythonu pro testovací scénář 24:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

driver = webdriver.Chrome()

try:
    print("Testovací scénář 24 spuštěn.")
    driver.get("http://sapfiorilaunchpadurl.com")

    # Krok 1: Log On
    print("Krok 1: Log On")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "LogOnButton"))).click()

    # Krok 2: Access the App
    print("Krok 2: Access the App")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ManageSalesOrders"))).click()

    # Krok 3: Navigate to Create Sales Order Screen
    print("Krok 3: Navigate to Create Sales Order Screen")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "CreateButton"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "CreateSalesOrderVA01"))).click()

    # Krok 4: Enter the Order Type OR (Standard Order)
    print("Krok 4: Enter the Order Type OR (Standard Order)")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "OrderType"))).send_keys("OR")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "SalesOrganization"))).send_keys("2010")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "DistributionChannel"))).send_keys("10")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Division"))).send_keys("00")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ContinueButton"))).click()

    # Krok 5: Enter Order Details
    print("Krok 5: Enter Order Details")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "SoldToParty"))).send_keys("20100001")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ShipToParty"))).send_keys("20100001")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "CustomerReference"))).send_keys("<PO number>")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "OrderReason"))).send_keys("<Order Reason>")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ReqDelivDate"))).send_keys(datetime.date.today() + datetime.timedelta(days=2))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "MaterialNumber"))).send_keys("FG228")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "OrderQuantity"))).send_keys("<Quantity>")

    # Krok 6: Save Document
    print("Krok 6: Save Document")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "SaveButton"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ContinueButton"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ApplyButton"))).click()

    print("Testovací scénář 24 úspěšně dokončen.")

except Exception as e:
    print("Při spuštění testovacího scénáře 24 došlo k chybě:")
    print(e)

finally:
    driver.quit()
```

Tento skript potřebuje, abyste dohledal správné jména prvků (NAME) pro metodu `.find_element_by_name()`. Tyto hodnoty jsou v tomto vzoru nahrazeny placeholdery.