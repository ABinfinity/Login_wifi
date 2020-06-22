#!/usr/local/bin python3.8


from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(options=chrome_options)
browser.get('http://176.10.10.1/login')#enter your wifi login page address

try:
    browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[1]/td[2]/input').send_keys('enter username here')#adjust the xpath with your username input field

    browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[2]/td[2]/input').send_keys('enter password here')#adjust the xpath with your passowrd input field

    browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[3]/td[2]/input').click()#adjust the xpath with your submit button

    browser.close()
    print('Login Successful')

except Exception as e:
    print(e)
    browser.close()
    print('Login Unsuccessful')
    
