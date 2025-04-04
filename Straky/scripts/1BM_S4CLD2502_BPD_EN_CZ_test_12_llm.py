```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializacia WebDriver-u, nastavenie cesty k driver-u.
driver = webdriver.Chrome('/path/to/chromedriver')

# Otvaranie webovej stranky.
driver.get('https://www.sap.com')

# Vyhladanie elementu a prihlasenie.
try:
    logon = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'logon_elem_id'))
    )
    logon.click()
except Exception as e:
    print(f'Logon element not found: {e}.')

# Otvorenie aplikácie.
try:
    access_app = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'access_app_id'))
    )
    access_app.click()
except Exception as e:
    print(f'Access app element not found: {e}.')

# Ziskaj element, skontroluj ci je toggle tlacidlo zapnute.
try:
    toggle_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'toggle_button_id'))
    )
    if not toggle_button.is_selected():
        toggle_button.click()
except Exception as e:
    print(f'Toggle button not found: {e}.')

# Zadaj material a zobraz Manage Materials.
try:
    search_material = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'search_material_id'))
    )
    search_material.send_keys('SG224')
    search_material.send_keys(Keys.RETURN)
except Exception as e:
    print(f'Search material not found: {e}.')

# Zobraz detaily materialu.
try:
    material_details = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'material_details_id'))
    )
    material_details.click()
except Exception as e:
    print(f'Material details not found: {e}.')

# Zobraz naplanovanú objednávku.
try:
    planned_order = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'planned_order_id'))
    )
    planned_order.click()
except Exception as e:
    print(f'Planned order not found: {e}.')

# Ukonci testovaci skript.
driver.quit()
```

Prosím upravte element IDs (napr. `'logon_elem_id'`, `'access_app_id'`) na správne ID elementu, ktorý chcete manipulovať. Takisto je potrebné nastaviť cestu k `chromedriver`.