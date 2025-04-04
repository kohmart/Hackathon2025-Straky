Následující skript v Pythonu používá Selenium WebDriver pro provedení testovacího scénáře. Předpokládá se, že pole "Duration" a "Responsibility" jsou textová pole na webové stránce. Identifikace těchto elementů (například jejich názvy nebo id) nebyly poskytnuty v testovacím scénáři, takže jsou nahrazeny "duration_id" a "responsibility_id".

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Inicializace WebDriveru
driver = webdriver.Firefox() 

# URL, na které má být přecházeno, nebylo poskytnuto v testovacím scénáři, 
# takže to je nahrazeno proměnnou "url"
url = "http://someurl.com"
driver.get(url)

try:
    # Čekání na pole Duration
    duration = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "duration_id"))
    )
 
    #Nastavení hodnoty pole Duration na prázdný řetězec
    duration.clear()
    duration.send_keys("")

    print("Krok 1: Nastavení pole Duration na prázdný řetězec bylo úspěšné")

except Exception as e:
    print("Krok 1: Chyba při nastavení pole Duration: ", str(e))

try:
    # Čekání na pole Responsibility
    responsibility = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "responsibility_id"))
    )

    # Nastavení hodnoty pole Responsibility
    responsibility.clear()
    responsibility.send_keys("<State the Service Provider, Customer or Joint Service Provider and Customer>")

    print("Krok 2: Nastavení pole Responsibility bylo úspěšné")

except Exception as e:
    print("Krok 2: Chyba při nastavení pole Responsibility: ", str(e))

# Zavření prohlížeče po testu
driver.quit()
```
Poznámky:

- Tento skript předpokládá, že sloužíte Firefox. Pokud ne, zmeňte `webdriver.Firefox()` na odpovídající prohlížeč (např. `webdriver.Chrome()`, `webdriver.Safari()`, atd.).
- Doporučuje se mít try/catch bloky kolem každé akce WebDriveru, protože pokud se něco pokazí, dá vám to konkrétní chybovou hlášku.
- `WebDriverWait` se používá k čekání na určité podmínky (např. dokud se prvek nezobrazí), což může pomoci zvládnout asynchronní chování webových stránek.