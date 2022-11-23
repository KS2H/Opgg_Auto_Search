import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Account
op_id = (open('id.txt', 'r')).readlines(0)[0]
op_pw = (open('password.txt', 'r')).readlines(0)[0]

# Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)

# Login
driver.get('https://member.op.gg/?redirect_url=//www.op.gg/')
driver.find_element(By.NAME, 'email').send_keys(op_id)
time.sleep(0.1)
driver.find_element(By.NAME, 'password').send_keys(op_pw)
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.member-card-layout__inner > div > form > button.member-button.login__btn').click()
time.sleep(1)

# search main
driver.find_element(By.XPATH, '//*[@id="__next"]/header/div[3]/nav/ul/li[2]/a').click()
