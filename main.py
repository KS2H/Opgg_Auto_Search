import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chamList import getChamLists

# Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)

# Account
op_id = (open('id.txt', 'r')).readlines(0)[0]
op_pw = (open('password.txt', 'r')).readlines(0)[0]

# Login
driver.get('https://member.op.gg/?redirect_url=//www.op.gg/')
driver.find_element(By.NAME, 'email').send_keys(op_id)
time.sleep(0.1)
driver.find_element(By.NAME, 'password').send_keys(op_pw)
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.member-card-layout__inner > div > form > button.member-button.login__btn').click()
time.sleep(1)

# search main
driver.get('https://www.op.gg/champions')
chamlist = getChamLists(driver)
answer = input('상대의 챔피언 이름을 입력하세요 : ')
search = str(chamlist.index(answer)+1)
cham = '//*[@id="content-container"]/div[2]/aside/nav/ul/li[' + search + ']/a'
driver.find_element(By.XPATH, cham).click()
driver.find_element(By.XPATH, '//*[@id="content-container"]/aside/div[2]/h3/a').click()
driver.find_element(By.XPATH, '//*[@id="content-container"]/aside/div[1]/div[2]/table/thead/tr/th[3]').click()   
driver.find_element(By.XPATH, '//*[@id="content-container"]/aside/div[1]/div[2]/table/thead/tr/th[3]').click()