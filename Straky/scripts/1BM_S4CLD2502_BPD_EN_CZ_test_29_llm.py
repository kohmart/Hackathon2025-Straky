Testovací skript v Pythonu může vypadat následovně:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# nahradit 'cesta_k_webdriveru' cestou k instalaci webdriveru
driver = webdriver.Firefox(executable_path='cesta_k_webdriveru')

try:
    driver.get('http://www.nějakáadresa.com')

    try:
        # krok 1: element Duration (nadefinovani elementu zavisle na jeho typu a lokalizaci)
        wait = WebDriverWait(driver, 10)
        duration = wait.until(EC.visibility_of_element_located((By.NAME, 'duration')))
        print("Element Duration nalezen")
    except Exception as e:
        print("Nepodarilo se najit Element Duration")
        print(str(e))

    try:
        # krok 2: element Responsibility
        responsibility = wait.until(EC.visibility_of_element_located((By.NAME, 'responsibility')))
        print("Element Responsibility nalezen")
        responsibility.send_keys("State the Service Provider, Customer or Joint Service Provider and Customer")
    except Exception as e:
        print("Nepodarilo se najit Element Responsibility")
        print(str(e))

finally:
    # zavrit prohlizec
    driver.quit()

```

Poznámka: Tento skript předpokládá, že elementy "Duration" a "Responsibility" jsou definovány pomocí atributu `name`. Pokud ne, musíte nahradit `By.NAME` příslušným selectorem (např. `By.ID`, `By.CLASS_NAME`, `By.XPATH` atd.).
U elementu "Duration" nebyla ve scénáři uvedena žádná hodnota, takže je pouze nalezen a nejsou s ním vykonávány žádné další akce.