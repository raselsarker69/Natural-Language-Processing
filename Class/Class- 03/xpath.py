from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Daraz Bangladesh website
driver.get('https://www.daraz.com.bd/routers/')
driver.maximize_window()

link_list = []

for i in range(1, 13):
    type_i = str(i)
    link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[' + type_i + ']/div/div/div[2]/div[2]/a').get_attribute('href')
    link_list.append(link)

print(link_list)

time.sleep(200)  # Wait for a few seconds to observe the browser
driver.quit()  # Close the browser