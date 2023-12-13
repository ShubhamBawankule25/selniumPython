from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

t.sleep(5)

text_box.send_keys("Selenium")
submit_button.click()

t.sleep(5)

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()
print(f"The page title is: {title}")
