Následující skript v Pythonu pomocí Selenium WebDriver představuje překlad uvedeného testovacího scénáře:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("URL SAP Fiori launchpad") # Doplnit URL
    print("Krok 1: Log On")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector log on buttonu>")) # Doplnit CSS selector
    ).click()
    
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector aplikace Monitor Material Coverage>")) # Doplnit CSS selector
    ).click()
    print("Krok 2: Access the App")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector uzivatelske ikony>")) # Doplnit CSS selector
    ).click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector dialogoveho okna MRP Settings>")) # Doplnit CSS selector
    )
    print("Krok 3: Check Default Setting")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector pole pro vlozeni Material>")) # Doplnit CSS selector
    ).send_keys("SG224")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector tlacitka Go>")) # Doplnit CSS selector
    ).click()
    print("Krok 4: Enter Relevant Search Criteria")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "<CSS selector tlacitka Home>")) # Doplnit CSS selector
    ).click()
    print("Krok 6: Back")

except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()
```
Poznámky:
- Z důvodu citlivosti dat a odlišností mezi jednotlivými SAP Fiori nastaveními je nutné doplnit vlastní URL a CSS selektory výše uvedených prvků.
- Bylo třeba vynechat Krok 5, protože v zadání nebyly poskytnuty žádné instrukce.
- Tento skript neobsahuje logování do souboru. Pokud je tato funkce požadována, musí být do skriptu přidána.