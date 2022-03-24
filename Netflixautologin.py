from selenium import webdriver

def selenium_test():
    Chrome_driver = 'C:/chromedriver.exe'
    driver = webdriver.Chrome(Chrome_driver)
    url = 'https://www.netflix.com/kr/login'
    driver.get(url)
    
    driver.find_element_by_id('id_userLoginId').send_keys('UserID')
    driver.find_element_by_id('id_password').send_keys('Password')
    driver.find_element_by_css_selector('#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button').click()
    while(True):
    	pass

selenium_test()


