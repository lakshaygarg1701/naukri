from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
RESUME_PATH = os.getenv("RESUME_PATH")

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def update_resume():
    try:
        driver.get("https://www.naukri.com/")
        time.sleep(3)

        # Click on login
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)

        # Enter email and password
        driver.find_element(By.NAME, "username").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD, Keys.RETURN)
        time.sleep(5)

        # Navigate to profile
        driver.get("https://www.naukri.com/mnjuser/profile?id=&orgn=homepage")
        time.sleep(5)

        # Upload new resume
        upload_btn = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_btn.send_keys(RESUME_PATH)
        time.sleep(5)

        print("Resume updated successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    update_resume()
