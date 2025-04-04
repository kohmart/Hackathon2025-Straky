from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json

# === Přihlašovací údaje ===
USERNAME = "P014920"
PASSWORD = "QEASd6GfazZu3Wp"
BUS_USERS_APP_URL = "https://my407083.s4hana.cloud.sap/ui#BusinessUser-maintain"

# === Spuštění Selenium ===
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BUS_USERS_APP_URL)

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

# === Počkat na načtení vstupních polí ===
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    print("✅ Aplikace Maintain Business Users načtena.")
except Exception as e:
    print(f"⚠️ Formulář nebyl načten: {e}")

# === Hledání polí z testovacího scénáře pomocí ID nebo aria-labelledby ===
search_fragments = {
    "First Name": "FirstNameMatchCode",
    "Last Name": "LastNameMatchCode"
}

matched_fields = []

# === Pro každý hledaný název proveď vyhledání ===
for label, fragment in search_fragments.items():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//input[contains(@id,'{fragment}') or contains(@aria-labelledby,'{fragment}')]"))
        )
        matched_fields.append({
            "field": label,
            "id": element.get_attribute("id"),
            "aria-labelledby": element.get_attribute("aria-labelledby"),
            "value": element.get_attribute("value"),
            "tag": element.tag_name,
            "class": element.get_attribute("class")
        })
        print(f"✅ Nalezeno pole pro: {label}")
    except Exception as e:
        print(f"❌ Nepodařilo se najít pole '{label}': {e}")

# === Uložit výstup ===
with open("bu_fields_from_scenario_by_id.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["field", "id", "aria-labelledby", "value", "tag", "class"])
    writer.writeheader()
    writer.writerows(matched_fields)

with open("bu_fields_from_scenario_by_id.json", "w", encoding="utf-8") as f:
    json.dump(matched_fields, f, indent=2, ensure_ascii=False)

print("📄 Uloženo: bu_fields_from_scenario_by_id.csv a .json")

# === Screenshot pro kontrolu ===
driver.save_screenshot("business_user_screen.png")

# === Ukončení ===
time.sleep(3)
driver.quit()
