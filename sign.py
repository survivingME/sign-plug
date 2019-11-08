from selenium import webdriver
import time
import utils

jd_sign_page = 'https://vip.jd.com/sign/index'
zdm_page = 'https://www.smzdm.com/'
zdm_login_button = '/html/body/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[1]/a'
zdm_sign_button = '/html/body/div[2]/div/div[3]/div[3]/div[2]/a'

print("start signing...")

# jd sign
browser = webdriver.Chrome()
jd_cookies = utils.read_jd_cookies()
browser.get(jd_sign_page)
browser.delete_all_cookies()
print("wait login page...")
time.sleep(2)
for cookie in jd_cookies:
    browser.add_cookie({
        "domain": ".jd.com",
        "name": cookie,
        "value": jd_cookies[cookie],
        "path": '/',
        "expires": None
    })
browser.get(jd_sign_page)
browser.maximize_window()
# todo: click sign button
print('no signature wait...')
time.sleep(2)

# zdm sign
browser.get(zdm_page)
zdm_cookies = utils.read_zdm_cookies()
browser.delete_all_cookies()
print("wait page...")
time.sleep(2)
for cookie in zdm_cookies:
    browser.add_cookie({
        "domain": ".smzdm.com",
        "name": cookie,
        "value": zdm_cookies[cookie],
        "path": '/',
        "expires": None
    })
browser.get(zdm_page)
# browser.maximize_window()
browser.find_element_by_xpath(zdm_sign_button).click()
print('no signature wait...')
time.sleep(2)
browser.quit()