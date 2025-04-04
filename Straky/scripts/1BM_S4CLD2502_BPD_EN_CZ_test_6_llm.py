Předpokládám, že všechny prvky jsou určeny tlačítky.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    # Krok 2
    print("Krok 2")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MaintainPIRs"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "ApplicationJobScreen"), "The Application Jobs screen displays.")
    )

    # Krok 3
    print("Krok 3")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ScheduleMRPRuns"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "ApplicationJobScreen"), "The Application Jobs screen displays.")
    )

    # Krok 4
    print("Krok 4")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MonitorMaterialCoverage"))
    ).click()

    # Krok 6
    print("Krok 6")
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "MonitorMaterialCoverageScreen"), "The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays.")
     )

    # Krok 7
    print("Krok 7")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ManageProductionOrders"))
    ).click()

    # Krok 8
    print("Krok 8")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ChangeProductionOrder"))
    ).click()

    # Ostatní kroky by se daly naprogramovat obdobným způsobem

except Exception as ex:
    print("Chyba: {}".format(str(ex)))

finally:
    driver.quit()
```
Prosím poznamenejte, že v kódu je použit předpoklad o struktuře webové stránky, např. ID prvku, kód může vypadat jinak pro jiné stránky nebo pokud má stránka jinou strukturu.