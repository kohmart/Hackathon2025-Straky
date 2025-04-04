Níže je uveden Selenium testovací skript v Pythonu na základě uvedeného testovacího scénáře:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

kroky = [
    ('FERT', 'PC'),
    ('SEMI', 'PC'),
    ('RAW', 'PC'),
    ('SEMI', 'PC'),
    ('RAW', 'PC'),
    ('SEMI', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
    ('SEMI', 'PC'),
    ('RAW', 'PC'),
    ('RAW', 'PC'),
]

try:
    for index, krok in enumerate(kroky, start=1):
        print(f'Krok {index}:')
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, krok[0]))
        )
        
        element.clear()
        element.send_keys(krok[1])
        
        print(f'Element: {krok[0]}, Hodnota: {krok[1]}')
        
        if index < len(kroky):
            # Předpokládá se, že každý krok přechází na novou stránku, takže čekáme, než se načte
            WebDriverWait(driver, 10).until(EC.staleness_of(element))
    
except Exception as ex:
    print(f'Nastala chyba: {ex}')
finally:
    driver.quit()
```

Poznámka: Tento kód předpokládá, že každý krok přechází na novou stránku. Pokud to není případ, měly by být upraveny čekání na elementy. Testovací scénář také neuvádí, co se stane po zadání hodnoty do pole, takže se kód pouze pokusí najít pole a zadat hodnotu.