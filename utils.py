from selenium import webdriver
import pickle
import time
import os

jd_login_page = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
zdm_page = 'https://www.smzdm.com/'
zdm_login_button = '/html/body/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[1]/a'


def get_zdm_cookies_m():
    browser = webdriver.Chrome()
    browser.get(zdm_page)
    print('wait web...')
    time.sleep(3)
    browser.maximize_window()
    browser.find_element_by_xpath(zdm_login_button).click()
    print('wait manual login...')
    time.sleep(10)
    # dump cookies
    print("start dumping cookies...")
    zdm_cookies = browser.get_cookies()
    browser.quit()
    cookies = {}
    for item in zdm_cookies:
        cookies[item['name']] = item['value']
    with open('zdm_cookies.pickle', 'wb') as f:
        pickle.dump(cookies, f)
    return cookies


def read_zdm_cookies():
    # if cookies file exists, use
    # if not , get_cookies()
    if os.path.exists('zdm_cookies.pickle'):
        with open('zdm_cookies.pickle', 'rb') as f:
            zdm_cookies = pickle.load(f)
        print("read cookies success...")
    else:
        zdm_cookies = get_zdm_cookies_m()
    return zdm_cookies


def get_jd_cookies():
    browser = webdriver.Chrome()
    browser.get(jd_login_page)
    print("wait web...")
    time.sleep(5)
    browser.maximize_window()
    print("wait QR code...")
    time.sleep(10)
    # dump cookies
    print("start dumping cookies...")
    jd_cookies = browser.get_cookies()
    browser.quit()
    cookies = {}
    for item in jd_cookies:
        cookies[item['name']] = item['value']
    with open('jd_cookies.pickle', 'wb') as f:
        pickle.dump(cookies, f)
    '''
    output_path = open('C://Users//1//Desktop//tsdm-plug-master//tsdm_cookies.pickle', 'wb')
    pickle.dump(cookies, output_path)
    output_path.close()
    '''
    return cookies


def read_jd_cookies():
    # if cookies file exists, use
    # if not , get_cookies()
    if os.path.exists('jd_cookies.pickle'):
        with open('jd_cookies.pickle', 'rb') as f:
            jd_cookies = pickle.load(f)
        print("read cookies success...")
        '''
        read_path = open('jd_cookies.pickle', 'rb')
        print("read cookies success...")
        tsdm_cookies = pickle.load(read_path)
        read_path.close()
        '''
    else:
        jd_cookies = get_jd_cookies()
    return jd_cookies
