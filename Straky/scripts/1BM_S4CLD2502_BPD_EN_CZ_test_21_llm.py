Předpokládám, že máme testovací web s formulářem, který obsahuje textová pole s atributem "name" pro "duration" a "responsibility". 

Vaši potřebu by mohl pokrýt následující kód:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def test_form_submission():
    try:
        driver = webdriver.Chrome()  # předpokládáme použití Chrome

        driver.get("http://example.com")  # předpokládáme, že testovací web je na této adrese

        # Čekání na načtení stránky
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'duration')))

        print("Stránka je načtená")

        # Vložení hodnoty do formuláře
        duration = driver.find_element_by_name('duration')
        duration.clear()
        duration.send_keys("120")

        responsibility = driver.find_element_by_name('responsibility')
        responsibility.clear()
        responsibility.send_keys("Service Provider")

        print("Hodnoty byly vloženy do formuláře")

        # Odeslání formuláře
        driver.find_element_by_name('submit').click()

        print("Formulář byl odeslán")

    except NoSuchElementException as ex:
        print(f"Element nenalezen: {ex}")

    except TimeoutException as ex:
        print(f"Čas vypršel: {ex}")

    except Exception as ex:
        print(f"Nastala neočekávaná chyba: {ex}")

    finally:
        # Ukončení prohlížeče
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
```

Poznámky:
1. Náš test předpokládá, že používáme Chrome prohlížeč. Pro jiný prohlížeč budete muset změnit `webdriver.Chrome()` na odpovídající řadič, např. `webdriver.Firefox()` pro Firefox.
2. Musíte mít nainstalovaný odpovídající prohlížeč a chromedriver/firefoxdriver atd. na cestě systému.
3. Předpokládáme, že testovací web je na adrese `http://example.com`. Změňte to na skutečnou adresu testovacího webu.
4. Předpokládáme, že ovládací prvek pro odeslání formuláře má atribut `name` nastaven na `submit`. To bude potřeba upravit podle skutečných detailů ovládacího prvku pro odeslání formuláře na vašem webu.
5. Namísto skutečných hodnot, které chcete vložit do "duration" a "responsibility", jsem použil demonstrační hodnoty `120` a `Service Provider`.
6. Kód je zamýšlen jako výchozí bod a bude potřebovat další úpravy a rafinaci podle konkrétních požadavků vašeho webu a testovacího scénáře.