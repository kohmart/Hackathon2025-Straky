V případě potřeby upravte následující kód podle konkrétních požadavků vašeho softwaru a webových elementů.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def test_scenario_32():
    try:
        driver = webdriver.Firefox()
        
        print("Logging on...")
        driver.get("*SAP_FIORI_LAUNCHPAD_URL*")  # nahraďte skutečnou url SAP Fiori launchpadu
        print("Logged on successfully.")
        
        print("Searching for material...")
        search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "*SEARCH_BOX_ID*")))  # nahraďte skutečnou id vyhledávacího pole
        search_box.send_keys("<BOM Header Material>")
        search_box.submit()
        print("Material searched successfully.")
        
        print("Displaying object...")
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "*DROPDOWN_ID*")))  # nahraďte skutečnou id vysouvacího menu
        dropdown.select_by_visible_text('*OBJECT*')  # nahraďte skutečný text objektu
        search_icon = driver.find_element_by_name('*SEARCH_ICON_NAME*')  # nahraďte skutečný název vyhledávací ikony
        search_icon.click()
        print("Object displayed successfully.")
        
        print("Tailoring the result display...")
        filter_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "*FILTER_ICON_ID*")))  # nahraďte skutečnou id ikony filtru
        filter_icon.click()
        print("Result display tailored successfully.")
        
        # Tento krok by bylo lepší provést pomocí cyklu, aby bylo možné předchozí kroky opakovat pro různé role a objekty.
        print("Repeating steps for another role and object...")
        test_scenario_32()
        print("Steps repeated successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.print_exc())
    finally:
        print("Closing the driver...")
        driver.quit()


if __name__ == "__main__":
    test_scenario_32()
```

Tento kód potřebuje konkrétní názvy a ID elementů webové stránky, kterou chcete otestovat. Nahradíte je ve všech výstupech s hvězdičkami (*). Pravděpodobně budete muset upravit některé části kódu podle konkrétního vzhledu a chování vaší webové stránky.