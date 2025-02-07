# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()

# # Open the Daraz Bangladesh website
# driver.get('https://www.daraz.com.bd/routers/')
# driver.maximize_window()


# for page in range(1, 16):  # First 15 pages
#     xpath = f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{page}]'
#     print(f"Page {page}: {xpath}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Daraz Bangladesh website
driver.get('https://www.daraz.com.bd/routers/')
driver.maximize_window()

try:
    # Loop through the first 15 pages
    for page in range(1, 16):  # First 15 pages
        # XPath for the pagination button
        xpath = f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{page}]'
        
        try:
            # Wait for the button to become clickable and click it
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
            
            print(f"Navigated to Page {page}")
            
            # Wait for the page to load (adjust if necessary)
            time.sleep(3)
        except Exception as e:
            print(f"Could not navigate to Page {page}: {e}")
finally:
    # Close the browser
    driver.quit()
