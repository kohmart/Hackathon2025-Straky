Zde je Python script pro tento scénář:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10) 

def input_text(element_id, text):
    try:
        element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
        element.clear()
        element.send_keys(text)
        print("Text '{}' was entered in the element with id '{}'".format(text, element_id))
    except Exception as e:
        print("An error occurred while trying to input text into the element with id '{}': ".format(element_id), str(e))

# the function simulates the steps of the scenario
def test_scenario():
    print("Test Scenario 9")
    input_text("duration", "")
    input_text("responsibility", "<State the Service Provider, Customer or Joint Service Provider and Customer>")

# start the scenario
if __name__ == "__main__":
    try:
        driver.get("http://www.example.com") # replace with the site url you want to test
        test_scenario()
    finally:
        driver.quit()
```

Tento skript používá WebDriver pro Firefox. Pokud chcete použít jiný prohlížeč, jednoduše nahraďte `webdriver.Firefox()` jiným ovladačem, například `webdriver.Chrome()`.

Použijte url cílové stránky místo `"http://www.example.com"`. Za předpokladu, že na stránce jsou elementy s id `"duration"` a `"responsibility"`, tento skript vyplní tyto elementy podle kroků uvedených v scénáři. Brání se výjimkám tím, že obklopí kritické kody blokem try-except. Také loguje své kroky pomocí `print`. 

Tento kód je nakonec kompletně spustitelný.
