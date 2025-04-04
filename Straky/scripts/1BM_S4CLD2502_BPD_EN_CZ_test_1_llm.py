Pro konverzí této scénáře do Selenium testovacího skriptu v Pythonu budeme předpokládat, že hodnoty jsou id elementů na stránce a chceme zkontrolovat, zda jsou správně zobrazeny.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def test_sap_roles():
    driver = webdriver.Firefox()  # může být jakýkoli ovladač podle preferencí, např. Chrome()
    driver.get('http://url-to-your-website.com')  # nahraďte prosím URL vaší webové stránky

    roles_map = {
        'SAP_BR_PRODN_PLNR': 'Production Planning',
        'SAP_BR_PRODN_SUPERVISOR_DISC': 'Production Management - Discrete Manufacturing',
        'SAP_BR_PRODN_OPTR_DISC': 'Production Execution - Discrete Manufacturing',
        'SAP_BR_WAREHOUSE_CLERK': 'Inventory Processing',
        'SAP_BR_INTERNAL_SALES_REP': 'Internal Sales / Billing / Customer Returns', 
        'SAP_BR_INVENTORY_MANAGER': 'Inventory Management',
        'SAP_BR_ADMINISTRATOR': 'Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Output Control'
    }

    try:
        for role_id, role_name in roles_map.items():
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, role_id)))
            assert element.text == role_name
            print(f"Element '{role_id}' s hodnotou '{role_name}' úspěšně nalezen")

    except TimeoutException as ex:
        print(f"Chyba: Element nebyl nalezen: {ex}")
    finally:
        driver.quit()

test_sap_roles()
```

Prosím, nezapomeňte nahradit `http://url-to-your-website.com` vlastní URL adresou testované webové stránky.

Můžete také upravit časový limit čekání dle potřeby (zde současných 10 sekund).

Výše uvedený skript prochází mapu rolí, čeká, až se objeví prvek s daným id, a poté kontroluje, zda text tohoto elementu odpovídá očekávaným hodnotám. Také zachází s výjimkami týkajícími se časových limitů a zaznamenává průběh testu. Na konci se ovladač ukončí.