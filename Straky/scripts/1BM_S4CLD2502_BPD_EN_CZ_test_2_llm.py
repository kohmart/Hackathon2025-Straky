Vzorový Selenium WebDriver skript v Pythonu může vypadat následovně:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://adresa-webu.com")  # nahradit pravou adresou

elements = {
    "FG228": "FIN228,MTO,PD,Fifo",
    "SG21": "SG21",
    "SG22": "SG22",
    "SG25": "SG25",
    "SG23": "SEMI23,PD,Subcontracting",
    "RM13": "RAW13,PD,Subcontracting",
    "RM14": "RAW14,PD,Subcontracting",
    "SG224": "SG224",
    "RM16": "RM16",
    "RM20": "RM20",
    "RM27": "RM27",
    "RM120": "RM120",
    "RM122": "RM122",
    "RM124": "RM124",
    "RM128": "RM128",
    # Ostatní elementy by měly být definované podobně, pokud je pro ně dostupné ID
}

try: 
    for id, value in elements.items():
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, id))
        )
        driver.find_element_by_id(id).send_keys(value)
        print(f"Vložení hodnoty '{value}' do elementu '{id}' proběhlo úspěšně.")
except Exception as e:
    print(str(e))
finally:
    driver.quit()
```

Tento kód projde přes všechny definované elementy ve slovníku `elements` a pokusí se do nich vložit definované hodnoty. Používá se WebDriverWait pro čekání na to, až se element objeví. 

Poznámka: Toto je jen příklad, který předpokládá, že elementy, které chceme naplnit, mají ID. Skutečný kód se může lišit podle nastavení webové stránky.