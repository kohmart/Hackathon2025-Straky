Níže je příklad, jak by mohl daný scénář vypadat:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get("URL_SAP_Fiori_launchpad")
    print("Navigating to SAP Fiori launchpad.")

    # Krok 1: Log On
    WebDriverWait(driver, 10).until(EC.title_is("SAP Fiori launchpad"))
    print("Successfully logged on to SAP Fiori launchpad")

    # Krok 2: Access the App
    app = driver.find_element_by_link_text("Schedule MRP Runs (F1339)")
    app.click()
    print("Accessing the 'Schedule MRP Runs (F1339)' app.")
    
    # Krok 3:  Create New Job
    create_button = driver.find_element_by_css_selector("button.create")
    create_button.click()
    print("Creating new job.")
    
    job_template = driver.find_element_by_name("Job Template")
    job_name = driver.find_element_by_name("Job Name")
    
    job_template.send_keys("Material Requirement Planning (MRP)")
    job_name.send_keys("MRP for FG228")
    print("Filling in Template Selection section.")

    # Ostatní kroky budou vypadat podobně, jednoduššei je obejít pole a pro každý prvek volat send_keys
    
    # Krok 4: Refresh Application Jobs List
    search_box = driver.find_element_by_name("search")
    search_button = driver.find_element_by_css_selector("button.search")
    
    search_box.send_keys("MRP for FG228")
    search_button.click()
    print("Searching for 'MRP for FG228' job.")

except Exception as e:
    print(f"Test failed: {str(e)}")

finally:
    driver.quit()
    print("Test session ended.")
```
Tento testovací skript se zaměřuje na automazaci testovacích kroků s využitím Selenium WebDriver a Pythonu. Provedené kroky jsou logovány pomocí print funkce. Podrobný popis očekávané interakce s webem je uveden v testovacím scénáři, konkrétní implementace by pak záležela na konkrétní struktuře a názvech elementů na webové stránce.