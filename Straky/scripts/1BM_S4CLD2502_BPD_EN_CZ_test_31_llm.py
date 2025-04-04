Testovací skript by mohl vypadat takto:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Vytvorime instanci webdriveru pro prohlizec Chrome
driver = webdriver.Chrome()

# Otevreme v prohlizeci web
driver.get("https://yourwebsite.com")

# Zachyceni jakychkoliv vyjimek
try:
    # Krok 1: Cekame na element "Duration" az se zobrazi a pak napiseme hodnotu
    print("[INFO] Waiting for 'Duration' element to be visible")
    duration = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Duration")))
    duration.clear()
    duration.send_keys("")

    # Krok 2: Cekame na element "Responsibility" az se zobrazi a potom napiseme hodnotu
    print("[INFO] Waiting for 'Responsibility' element to be visible")
    responsibility = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Responsibility")))
    responsibility.clear()
    responsibility.send_keys("<State the Service Provider, Customer or Joint Service Provider and Customer>")

    print("[SUCCESS] Test passed")

except Exception as e:
    # Pokud se objevi jakakoli vyjimka, vypiseme ji a ozname chybu v testu
    print("[ERROR] An exception occurred: " + str(e))
    print("[FAILED] Test failed")

finally:
    # Na konci testu zavreme prohlizec
    driver.quit()
```

Upravte prosím `https://yourwebsite.com` na adresu vašeho webu a všechny ostatni identifikátory elementů na správné hodnoty.

Upozorňuji, že některé elementy mohou mít jiný typ identifikátoru namísto `By.NAME`. Mohlo by to být například `By.ID`, `By.CLASS_NAME`, `By.CSS_SELECTOR`, atd. V závislosti na tom, jak je strukturován váš webový kód. Ujistěte se, že používáte správné identifikátory.