from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Nastavení přihlašovacích údajů ===
USERNAME = "P014920"
PASSWORD = "QEASd6GfazZu3Wp"

# === SAP Fiori URL ===
BASE_URL = "https://my407083.s4hana.cloud.sap/ui#SalesQuotation-manage"
FIORI_APP_URL = "https://my407083.s4hana.cloud.sap/ui#SalesQuotation-manage"

# === Spuštění Chrome driveru ===
driver = webdriver.Chrome()
driver.maximize_window()

# === 1. Otevři login stránku ===
driver.get(BASE_URL)

# === 2. Počkat na zobrazení přihlašovacího formuláře ===
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "j_username"))
)

# === 3. Vyplnit login údaje ===
driver.find_element(By.NAME, "j_username").send_keys(USERNAME)
driver.find_element(By.NAME, "j_password").send_keys(PASSWORD)
time.sleep(1)  # Krátká pauza pro stabilitu
driver.find_element(By.ID, "logOnFormSubmit").click()

print("✅ Přihlášení odesláno...")

"""
# === 4. Počkat na přihlášení ===
WebDriverWait(driver, 30).until(
    lambda d: "shell" in d.current_url
)
"""

print("✅ Přihlášení úspěšné.")

# === 5. Načíst konkrétní Fiori aplikaci ===
driver.get(FIORI_APP_URL)
print(f"🔄 Načítám aplikaci: {FIORI_APP_URL}")

# === 6. Počkat na inicializaci SAPUI5 ===
WebDriverWait(driver, 60).until(
    lambda d: d.execute_script("return typeof sap !== 'undefined' && sap.ui.getCore().isInitialized()")
)

print("✅ SAPUI5 je inicializováno.")

# === 7. Najít <bdi> Go a kliknout na jeho tlačítko ===
try:
    create_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='Create Quotation']"))
    )
    create_button.click()
    print("👉 Kliknutí na tlačítko Create Quotation provedeno.")
except Exception as e:
    print(f"⚠️ Kliknutí na tlačítko Create Quotation selhalo: {e}")

# === 8. Ukončit test ===
time.sleep(3)
driver.quit()
