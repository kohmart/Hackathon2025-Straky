from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import json
from docx import Document
import openai
import random

# === OpenAI API klíč ===
openai.api_key = "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"  # ← ❗️nahraď svým klíčem nebo načítej z prostředí

# === Cesta k Word dokumentu ===
DOCX_PATH = r"C:\Hackathon\Straky\docx\BU-simple.docx"

# === Přihlašovací údaje ===
USERNAME = "P014920"
PASSWORD = "QEASd6GfazZu3Wp"
BUS_USERS_APP_URL = "https://my407083.s4hana.cloud.sap/ui#BusinessUser-maintain"

# === Spuštění Selenium ===
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BUS_USERS_APP_URL)

# === Přihlášení ===
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "j_username")))
driver.find_element(By.NAME, "j_username").send_keys(USERNAME)
driver.find_element(By.NAME, "j_password").send_keys(PASSWORD)
time.sleep(1)
driver.find_element(By.ID, "logOnFormSubmit").click()
print("✅ Přihlášení odesláno...")

# === Počkat na inicializaci SAPUI5 ===
try:
    WebDriverWait(driver, 60).until(lambda d: d.execute_script("return typeof sap !== 'undefined' && sap.ui.getCore().isInitialized()"))
    print("✅ SAPUI5 je inicializováno.")
except Exception as e:
    print(f"⚠️ SAPUI5 se nenačetlo: {e}")

# === Počkat na načtení vstupních polí ===
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    print("✅ Aplikace Maintain Business Users načtena.")
except Exception as e:
    print(f"⚠️ Formulář nebyl načten: {e}")

# === Načti text z Word dokumentu ===
def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

word_text = extract_text_from_docx(DOCX_PATH)

# === Získej test data z OpenAI ===
print("🧠 Posílám dokument do OpenAI...")
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "Jsi API parser. Vrať výstup výhradně ve formátu čistého validního JSON bez vysvětlení."},
        {"role": "user", "content": f"Z dokumentu:\n{word_text}\n\nVrať pouze JSON se vstupními hodnotami do SAP Fiori formuláře Business Users, např.: {{\"First Name\": \"Jan\", \"Last Name\": \"Strakoš\"}}"}
    ],
    temperature=0.2
)


gpt_reply = response["choices"][0]["message"]["content"]
print("📥 OpenAI odpověď:")
print(gpt_reply)

# === Pokus o převod odpovědi na dict ===
import json

try:
    raw_content = response["choices"][0]["message"]["content"].strip()
    start = raw_content.find('{')
    end = raw_content.rfind('}') + 1
    clean_json = raw_content[start:end]
    test_data = json.loads(clean_json)
except Exception as e:
    print(f"❌ Nepodařilo se načíst JSON z OpenAI odpovědi: {e}")
    print("🧪 Výchozí fallback: Jan / Strakoš")
    test_data = {"First Name": "Jan", "Last Name": "Strakoš"}

# === Fragmnety ID pro SAP Fiori pole ===
fragment_map = {
    "First Name": "FirstNameMatchCode",
    "Last Name": "LastNameMatchCode"
}

matched_fields = []

# === Vyhledání polí a vyplnění hodnot ===
for label, value in test_data.items():
    fragment = fragment_map.get(label, "")
    try:
        input_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//input[contains(@id,'{fragment}') or contains(@aria-labelledby,'{fragment}')]"))
        )
        input_field.clear()
        input_field.send_keys(value)
        matched_fields.append({
            "field": label,
            "id": input_field.get_attribute("id"),
            "aria-labelledby": input_field.get_attribute("aria-labelledby"),
            "value": value,
            "tag": input_field.tag_name,
            "class": input_field.get_attribute("class")
        })
        print(f"✅ Vyplněno pole '{label}' hodnotou '{value}'")
    except Exception as e:
        print(f"❌ Nepodařilo se vyplnit pole '{label}': {e}")

# === Kliknutí na tlačítko Go ===
try:
    go_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//bdi[normalize-space()='Go']]"))
    )
    go_button.click()
    print("🚀 Kliknutí na tlačítko Go provedeno.")
except Exception as e:
    print(f"❌ Tlačítko Go nenalezeno nebo nelze kliknout: {e}")

# === Uložení výstupů ===
with open("bu_fields_from_scenario_by_id.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["field", "id", "aria-labelledby", "value", "tag", "class"])
    writer.writeheader()
    writer.writerows(matched_fields)

with open("bu_fields_from_scenario_by_id.json", "w", encoding="utf-8") as f:
    json.dump(matched_fields, f, indent=2, ensure_ascii=False)

print("📄 Uloženo: bu_fields_from_scenario_by_id.csv a .json")

# === Screenshot ===
driver.save_screenshot("business_user_screen.png")

# === Druhé vyhledání s náhodným jménem a prázdným příjmením ===
random_names = ["Adam", "Eva", "Petr", "Marie", "Jan", "Jana", "Tomáš", "Lucie", "David", "Kateřina"]
random_first_name = random.choice(random_names)

# === Pomocná funkce pro odstranění všech tokenů ===
def clear_all_tokens_for_field(fragment):
    try:
        tokenizer_xpath = f"//div[contains(@id,'{fragment}-content')]//div[contains(@class,'sapMTokenizer')]"
        tokenizer = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, tokenizer_xpath))
        )
        tokens = tokenizer.find_elements(By.XPATH, ".//div[contains(@class,'sapMToken')]")
        print(f"🧹 Nalezeno tokenů pro '{fragment}': {len(tokens)}")
        for token in tokens:
            try:
                remove_icon = token.find_element(By.CLASS_NAME, "sapMTokenIcon")
                driver.execute_script("arguments[0].click();", remove_icon)
                time.sleep(0.2)
            except Exception as inner_e:
                print(f"⚠️ Token nešlo odstranit: {inner_e}")
    except Exception as e:
        print(f"❌ Tokenizer nebyl nalezen pro '{fragment}': {e}")

# === Seznam jmen pro náhodný výběr ===
random_names = ["Adam", "Eva", "Petr", "Marie", "Jan", "Jana", "Tomáš", "Lucie", "David", "Kateřina"]

# === Proveď test 10× ===
for i in range(1, 11):
    print(f"\n--- 🔁 Iterace {i}/10 ---")

    # Vymazání tokenů
    try:
        clear_all_tokens_for_field(fragment_map['First Name'])
        clear_all_tokens_for_field(fragment_map['Last Name'])
        print("✅ Tokeny byly odstraněny")
    except Exception as e:
        print(f"❌ Chyba při mazání tokenů: {e}")

    # Náhodné jméno
    random_first_name = random.choice(random_names)

    # Vyplnění náhodného jména
    try:
        first_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//input[contains(@id,'{fragment_map['First Name']}') or contains(@aria-labelledby,'{fragment_map['First Name']}')]"))
        )
        first_name_field.click()
        first_name_field.send_keys(random_first_name)
        time.sleep(0.3)
        driver.execute_script("arguments[0].blur();", first_name_field)
        print(f"✅ Iterace {i}: Vyplněno jméno '{random_first_name}'")
    except Exception as e:
        print(f"❌ Iterace {i}: Nepodařilo se vyplnit jméno: {e}")

    # Kliknutí na tlačítko Go
    try:
        go_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//bdi[normalize-space()='Go']]"))
        )
        go_button.click()
        print("🚀 Iterace {i}: Kliknutí na Go provedeno.")
    except Exception as e:
        print(f"❌ Iterace {i}: Tlačítko Go nenalezeno nebo nelze kliknout: {e}")

    # Screenshot pro daný běh
    screenshot_name = f"business_user_screen_iter_{i}.png"
    driver.save_screenshot(screenshot_name)
    print(f"📸 Screenshot uložen: {screenshot_name}")

    time.sleep(1)

# === Ukončení ===
time.sleep(2)
driver.quit()