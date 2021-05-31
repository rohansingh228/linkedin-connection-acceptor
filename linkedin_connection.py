import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

email = "Your EMAIL here"
password = "Your PASSWORD here"
# email = os.getenv('linkedin_email')
# password = os.getenv('linkedin_password')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.linkedin.com/login")

driver.find_element_by_id('username').send_keys(email)
driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_class_name('btn__primary--large').click()

driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

accept_button_list = []
while len(accept_button_list) == 0:
    accept_button_list = driver.find_elements_by_xpath(
        "//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")


for button in accept_button_list:
    button.click()
time.sleep(6)

# driver.close()
