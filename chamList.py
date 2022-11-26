from selenium.webdriver.common.by import By

def getChamLists(webdriver):
    return_list = []
    chams = webdriver.find_elements(By.XPATH, '//*[@id="content-container"]/div[2]/aside/nav/ul/li')
    for i in range(1, len(chams) + 1):
        chams_span_xpath = '//*[@id="content-container"]/div[2]/aside/nav/ul/li[' + str(i) + ']/a/span'
        chams_span_text = webdriver.find_element(By.XPATH, chams_span_xpath).text
        print('roading : [' + str(i) + '/' + str(len(chams)) + '] ')
        return_list.append(chams_span_text)
    return return_list