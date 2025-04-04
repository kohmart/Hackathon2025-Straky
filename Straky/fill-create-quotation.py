from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Přihlašovací údaje ===
USERNAME = "P014920"
PASSWORD = "QEASd6GfazZu3Wp"
CREATE_QUOTATION_URL = "https://my407083.s4hana.cloud.sap/ui#SalesQuotation-create?sap-app-origin-hint="

# === Spuštění prohlížeče ===
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(CREATE_QUOTATION_URL)

# === Přihlášení ===
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "j_username"))
)
driver.find_element(By.NAME, "j_username").send_keys(USERNAME)
driver.find_element(By.NAME, "j_password").send_keys(PASSWORD)
time.sleep(1)
driver.find_element(By.ID, "logOnFormSubmit").click()
print("✅ Přihlášení odesláno...")

# === Počkat na inicializaci SAPUI5 ===
try:
    WebDriverWait(driver, 60).until(
        lambda d: d.execute_script("return typeof sap !== 'undefined' && sap.ui.getCore().isInitialized()")
    )
    print("✅ SAPUI5 je inicializováno.")
except Exception as e:
    print(f"⚠️ SAPUI5 se nenačetlo: {e}")

# === Vyplnění pole Quotation Type podle title ===
try:
    element_id = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@title='Sales Document Type']"))
    ).get_attribute("id")

    # Vyplnění pomocí JS
    driver.execute_script(f"document.getElementById('{element_id}').value = 'QT';")
    print("✅ Pole 'Sales Document Type' vyplněno pomocí JavaScriptu.")
except Exception as e:
    print(f"⚠️ Nepodařilo se vyplnit pole pomocí JavaScriptu: {e}")

driver.save_screenshot("quotation_type_debug.png")
print("📸 Uložen screenshot jako 'quotation_type_debug.png'")

# === Konec testu ===
time.sleep(5)
driver.quit()
