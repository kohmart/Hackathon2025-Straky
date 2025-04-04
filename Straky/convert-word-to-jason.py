# --- Word to JSON & Selenium Test Generator ---
# Extracts 'Test Procedures' from SAP Fiori Word documents and outputs structured JSON and Selenium Python test scripts.

import docx
import json
import os
import re
from typing import List, Dict


def load_docx(path: str):
    return docx.Document(path)


def extract_test_procedures(doc) -> List[Dict]:
    cases = []
    current_case = None
    capture = False
    in_test_section = False

    for para in doc.paragraphs:
        text = para.text.strip()

        # Start capturing after finding 'Test Procedures'
        if 'Test Procedures' in text:
            in_test_section = True
            continue

        # Stop capturing if appendix or new major section begins
        if in_test_section and re.match(r"^\d+\s+Appendix", text):
            break

        if in_test_section:
            if re.match(r"^\d+\.\d+\.\d+.*", text):
                if current_case:
                    cases.append(current_case)
                current_case = {
                    "title": text,
                    "steps": []
                }
                capture = True
                continue

            if capture and text:
                if any(keyword in text.lower() for keyword in ["log on", "open", "enter", "create", "click", "submit"]):
                    current_case["steps"].append(text)

    if current_case:
        cases.append(current_case)

    return cases


def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_selenium_script(test_cases: List[Dict], output_path: str):
    for case in test_cases:
        title_safe = re.sub(r'[^a-zA-Z0-9_]', '_', case['title'])
        file_path = os.path.join(output_path, f"test_{title_safe}.py")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Selenium Test Case ---
driver = webdriver.Chrome()
driver.get("https://fiori.your-company.com")  # Update to real Fiori URL
time.sleep(3)

""")
            for step in case['steps']:
                comment = f"# {step}"
                f.write(f"{comment}\n")
                f.write("time.sleep(1)\n")

            f.write("""

print("✅ Test finished")
driver.quit()
""")


def convert_all_docs(input_folder: str, output_json_folder: str, output_code_folder: str):
    if not os.path.exists(output_json_folder):
        os.makedirs(output_json_folder)
    if not os.path.exists(output_code_folder):
        os.makedirs(output_code_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx"):
            filepath = os.path.join(input_folder, filename)
            print(f"📄 Processing: {filename}")
            try:
                doc = load_docx(filepath)
                cases = extract_test_procedures(doc)

                output_filename = filename.replace(".docx", ".json")
                json_path = os.path.join(output_json_folder, output_filename)
                save_json(cases, json_path)

                generate_selenium_script(cases, output_code_folder)
                print(f"✅ Output saved: {output_filename} + test scripts")
            except Exception as e:
                print(f"❌ Error with {filename}: {e}")


# --- Run Batch ---
if __name__ == "__main__":
    input_folder = "./Straky/test_scenarios"
    output_json_folder = "./Straky/output_json"
    output_code_folder = "./Straky/output_tests"

    convert_all_docs(input_folder, output_json_folder, output_code_folder)
