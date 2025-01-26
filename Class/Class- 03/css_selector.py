from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()


# Open the Daraz Bangladesh website
driver.get("https://www.daraz.com.bd/routers/")
driver.maximize_window()
    
    
# # link = driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.ICdUp > div > a')
# # print(link.get_attribute("href"))
# #driver.get(link.get_attribute("href"))



link_list = []

for i in range(1, 41):
    
    type_i = str(i)
    # Corrected CSS Selector (based on your style)
    link = driver.find_element(By.CSS_SELECTOR, f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child({type_i}) > div > div > div.ICdUp > div > a')
    print(link.get_attribute('href'))
    driver.get(link.get_attribute('href'))
    #link_list.append(link.get_attribute('href'))  # Save the link as a string
    link_list.append(link)  # Save the link as a string
    

print(link_list)

time.sleep(200)  # Wait for observation
driver.quit()  # Close the browser
