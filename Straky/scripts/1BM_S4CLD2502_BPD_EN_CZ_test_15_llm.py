Selenium skript v Pythonu by mohl vypadat následovně:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox() # Nebo jiný prohlížeč jako Chrome, Safari, atd...

try:
    driver.get('http://example.com') # Upřesněte adresu stránky

    print('Looking for duration element...')
    duration_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'duration_id')) # Nahradit správným ID
    )
    print('Duration element found.')
    # Nebyla uvedena hodnota, takže předpokládám, že máme pouze zkontrolovat přítomnost


    print('Looking for responsibility field...')
    responsibility_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'responsibility_id')) # Nahradit správným ID
    )
    print('Responsibility field found.')
    responsibility_value = "<State the Service Provider, Customer or Joint Service Provider and Customer>".strip()
    responsibility_field.send_keys(responsibility_value)

except Exception as e:
    print(f'Exception occurred: {e}')

finally:
    driver.quit()
```

Toto je základní test, který zkontroluje, zda pole "Duration" existuje a jestli je možné do pole "Responsibility" zapsat hodnotu.+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
V testu se předpokládá, že stránka existuje a že ID elementů jsou známy. Dále jsou přítomny základní pokyny pro logování a kontrolu výjimek pro zjednodušení řešení problémů během testování.

Pamatujte na to, že konkrétní cesty k elementům a jejich ID se mohou lišit podle struktury a designu vaší webové stránky, takže nahraďte 'duration_id' a 'responsibility_id' skutečnými ID elementů, které potřebujete otestovat.