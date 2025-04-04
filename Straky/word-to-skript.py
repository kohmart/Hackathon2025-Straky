import os
import subprocess
from pathlib import Path
from docx import Document
import openai

# Nastaveni OpenAI API klice (muze byt nacteno z .env souboru)
openai.api_key = "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"

# Vstupni a vystupni slozky
input_folder = r"C:\\Hackathon\\Straky\\docx"
output_folder = r"C:\\Hackathon\\Straky\\scripts"
os.makedirs(output_folder, exist_ok=True)

# URL testovane aplikace
test_url = "https://my407083.s4hana.cloud.sap/ui#Shell-home"

# Funkce pro extrakci testovacich kroku z Word dokumentu jako plain-text
def extract_test_scenarios_text(doc_path):
    doc = Document(doc_path)
    scenarios = []
    scenario_index = 1

    for table in doc.tables:
        steps_text = f"Testovací scénář {scenario_index} (URL: {test_url}):\n"
        valid_row_found = False

        for i, row in enumerate(table.rows[1:], start=1):  # Preskoceni hlavicky
            cells = row.cells
            if len(cells) < 4:
                print(f"⚠️  Přeskočen neúplný řádek {i} v souboru {doc_path}")
                continue
            action = cells[1].text.strip()
            element = cells[2].text.strip()
            value = cells[3].text.strip()
            steps_text += f"  Krok {i}: {action}, Element: {element}, Hodnota: {value}\n"
            valid_row_found = True

        if valid_row_found:
            scenarios.append(steps_text)
            scenario_index += 1

    return scenarios

# Funkce pro vygenerovani Selenium skriptu pomoci LLM
# def generate_script_from_llm(test_text):
#     prompt = f"""
# Preved nasledujici testovaci scenar na Selenium testovaci skript v Pythonu:
# 
# {test_text}
# 
# Pozadavky:
# - Pouzij knihovnu Selenium WebDriver
# - Pridej cekani na elementy (WebDriverWait)
# - Osetri vyjimky
# - Pridej logovani (print)
# - Kod musi byt kompletní a spustitelny
# - Prvni krok testu musi byt prihlaseni do SAP S/4HANA aplikace na URL {test_url}
# - Predpokladej, ze prihlasovaci formular obsahuje policka s ID "j_username" a "j_password" a tlacitko s ID "logOnFormSubmit"
# - Pouzij testovaci prihlasovaci udaje "test_user" a "test_password"
# """
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response["choices"][0]["message"]["content"]

# Funkce pro validaci skriptu (zkontroluje, zda obsahuje hlavni cast kodu)
def validate_script_content(script_text):
    required_keywords = ["webdriver", "By", "driver.get", "driver.quit"]
    return all(keyword in script_text for keyword in required_keywords)

# Funkce pro spusteni skriptu a zachyceni vystupu
def run_script(script_path):
    print(f"🚀 Spoustim test: {script_path.name}")
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    print("Výstup:")
    print(result.stdout)
    if result.stderr:
        print("Chyby:")
        print(result.stderr)

# Zpracovani vsech .docx souboru v adresari
def process_all_documents():
    for docx_file in Path(input_folder).glob("*.docx"):
        print(f"\U0001F4C4 Zpracovavam: {docx_file.name}")
        scenarios = extract_test_scenarios_text(docx_file)

        for idx, scenario in enumerate(scenarios, start=1):
            try:
                print(f"🔎 Připraveno pro generování: scénář {idx}\n{scenario}")
                # script_code = generate_script_from_llm(scenario)
                # if not validate_script_content(script_code):
                #     print(f"⚠️  Vygenerovaný skript pro {docx_file.name}, scénář {idx} vypadá nekompletní.")
                #     continue
                # output_path = Path(output_folder) / f"{docx_file.stem}_test_{idx}_llm.py"
                # with open(output_path, "w", encoding="utf-8") as f:
                #     f.write(script_code)
                # print(f"✅ Vygenerovano: {output_path}")
                # run_script(output_path)
            except Exception as e:
                print(f"❌ Chyba pri zpracovani {docx_file.name}, scenar {idx}: {e}")

    print("\U0001F389 Hotovo! Pripraveno k testovani prihlaseni.")

# Spusteni
if __name__ == "__main__":
    process_all_documents()
