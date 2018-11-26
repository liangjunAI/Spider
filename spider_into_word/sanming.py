#-*- encoding:utf-8 -*-

import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def driver_open():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"]=(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    )
    driver = webdriver.PhantomJS(executable_path='D:/data/phantomjs.exe',desired_capabilities=dcap)

    driver_item = webdriver.Chrome()
    return driver,driver_item

def get_content(driver,driver_item,url):
    content = driver_item.get(url)
    wait = ui.WebDriverWait(driver_item, 15)
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='row pgStyle']"))
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='searchContent']//div[@class='record row']"))
    list = driver_item.find_elements_by_xpath("//div[@class='searchContent']//div[@class='record row']")
    url_list = []
    for i in list:
        url = i.find_element_by_xpath("//div[@class=' recordTit']//a")
        url =url.get_attribute('href')
        print url

    return 1

if __name__=='__main__':
    driver,driver_item = driver_open()
    url = "http://rsj.sm.gov.cn/search/?key=%E5%85%BB%E8%80%81"
    content = get_content(driver,driver_item,url)

