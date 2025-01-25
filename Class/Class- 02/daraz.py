from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()


# Open the Daraz Bangladesh website
driver.get("https://www.daraz.com.bd/")
driver.maximize_window()


link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a')
print(link.get_attribute("href"))

driver.get(link.get_attribute("href"))
time.sleep(200)  # Wait for a few seconds to observe the browser
driver.quit()  # Close the browser
