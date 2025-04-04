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
CREATE_QUOTATION_URL = "https://my407083.s4hana.cloud.sap/ui#SalesQuotation-create?sap-app-origin-hint="

# === Spuštění Selenium ===
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

# === Čekání na SAPUI5 ===
try:
    WebDriverWait(driver, 60).until(
        lambda d: d.execute_script("return typeof sap !== 'undefined' && sap.ui.getCore().isInitialized()")
    )
    print("✅ SAPUI5 je inicializováno.")
except Exception as e:
    print(f"⚠️ SAPUI5 se nenačetlo: {e}")

# === Testovací pole z dokumentu (hledáme podle title) ===
titles_to_find = [
    "Sales Document Type",
    "Sales Organization",
    "Distribution Channel",
    "Division",
    "Sold-To Party",
    "Ship-To Party",
    "Customer Reference",
    "Customer Reference Date",
    "Requested Delivery Date",
    "Valid To",
    "Material",
    "Order Quantity"
]

found_fields = []

# === Vyhledání elementů podle title ===
for title in titles_to_find:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//input[@title='{title}']"))
        )
        found_fields.append({
            "label": title,
            "id": element.get_attribute("id"),
            "tag": element.tag_name,
            "title": element.get_attribute("title"),
            "value": element.get_attribute("value"),
            "type": element.get_attribute("type"),
            "class": element.get_attribute("class")
        })
        print(f"✅ Nalezeno pole: {title}")
    except:
        print(f"❌ Pole '{title}' nebylo nalezeno.")

# === Uložení výstupů ===
with open("found_fields_by_title.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["label", "id", "tag", "title", "value", "type", "class"])
    writer.writeheader()
    writer.writerows(found_fields)

with open("found_fields_by_title.json", "w", encoding="utf-8") as f:
    json.dump(found_fields, f, indent=2, ensure_ascii=False)

print("📄 Výstupy uloženy: found_fields_by_title.csv a found_fields_by_title.json")

# === Screenshot pro kontrolu ===
driver.save_screenshot("fields_by_title_screenshot.png")

# === Konec ===
time.sleep(3)
driver.quit()
