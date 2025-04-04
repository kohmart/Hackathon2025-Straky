
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Selenium Test Case ---
driver = webdriver.Chrome()
driver.get("https://fiori.your-company.com")  # Update to real Fiori URL
time.sleep(3)

# 4.1	Create Sales Order with Configurable Material	9
time.sleep(1)


print("✅ Test finished")
driver.quit()
