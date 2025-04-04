Níže je uveden příklad Selenium skriptu v Pythonu, který splňuje výše uvedené požadavky:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

try:
    # Initialize webdriver and load webpage
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")  # replace with your URL
    print("Web page is loaded")

    # Step 1: Log On
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login_button'))).click()
    print("Logged in")

    # Step 2: Access the App
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'app_button'))).click()
    print("App accessed")

    # Step 3: Check Default Area of Responsibility (Supervisor)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'user_icon'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'app_settings'))).click()
    print("App settings checked and modified")

    # Step 4: Select Production Order
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'filter_button'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'search_field'))).send_keys("SG224")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'search_button'))).click()
    print("Selected production order")

    # And so on for remaining steps...

except NoSuchElementException:
    print("Element not found")

finally:
    # Always end the session
    driver.quit()

```

Poznámka: Nahradil jsem všechen text místa pro uchování tlačítek, pole apod. Identifikátory ("login_button", "app_button" atd.) jsou jen náhodné jména, které jsem použil pro demonstraci. Musíte je nahradit skutečnými identifikátory prvků stránky, které chcete ovládat. Strukturu a logiku skriptu by však mělo být možné použít tak, jak je.

Prvky na stránce mohou být identifikovány různými způsoby, například pomocí jejich ID, názvu třídy, css selektoru, atd. Jaký způsob použijete, záleží na konkrétní webové stránce, se kterou pracujete.