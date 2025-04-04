Zde je Selenium WebDriver skript v Pythonu, který napodobuje uvedený testovací scénář. Mějte na paměti, že tento skript je vytvořený bez přístupu k konkrétní webové stránce nebo aplikaci a může vyžadovat další úpravy pro plnou funkčnost:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_scenario_10():
    driver = webdriver.Firefox()   # Používejte svůj preferovaný prohlížeč 

    try:
        # Krok 1: Log On
        driver.get("URL_SAP_FIORI_LAUNCHPAD") # Zadejte URL pro SAP Fiori launchpad
        print("Logging on to the SAP Fiori launchpad as a Production Planner...")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ELEMENT_ID'))) # Nahraďte ELEMENT_ID vašim konkrétním prvkem
        print("Successfully logged on to the SAP Fiori launchpad.")

        # Krok 2: Access the App
        driver.get('URL_APP') # Zadejte URL pro Schedule MRP Runs (F1339)
        print("Accessing the SAP Fiori App...")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ELEMENT_ID'))) # Nahraďte ELEMENT_ID vašim konkrétním prvkem
        print("Successfully accessed the SAP Fiori App.")
        
        # Krok 3: Create New Job
        print("Creating new job...")
        
        # TODO: Podrobný krok pro tvoření nové úlohy.
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ELEMENT_ID'))) # Nahraďte ELEMENT_ID vašim konkrétním prvkem
        print("New job created successfully.")

        # Krok 4: Refresh Application Jobs List
        print("Refreshing Application Jobs List...")
        
        # TODO: Krok pro obnovení seznamu úloh aplikace.

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ELEMENT_ID'))) # Nahraďte ELEMENT_ID vašim konkrétním prvkem
        print("Successfully refreshed the Application Jobs List.")

    except NoSuchElementException as e:
        print(f"An error occurred: {e}")
    except TimeoutException as e:
        print(f"Loading took too much time! {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_scenario_10()
```

Všimněte si, že musíte nahradit URL_SAP_FIORI_LAUNCHPAD, URL_APP a ELEMENT_ID reálnými hodnotami podle vaší konkrétní aplikace. Vzhledem k tomu, že tato ukázka kódu není specifická pro vaše prostředí, budou pravděpodobně potřeba úpravy pro konkrétní prvky, ovládací prvky a navigaci ve vaší aplikaci.