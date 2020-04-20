"""
后期维护批发物价数据库时，使用此文件来更新
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pymongo

# 地址，不弹出窗口，设置browser
url = 'http://zdscxx.moa.gov.cn:8080/misportal/public/agricultureIndexRedStyle.jsp'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities['pageLoadStrategy'] = "none"
browser = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
browser.get(url)
wait = WebDriverWait(browser, 100)

# 数据库准备操作
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.rept
all_num = [1, 9, 19, 59]
point_num = [7, 9, 30, 8]
col = ['meat', 'aqua', 'vege', 'frut']


def reptile():      # 获得大分类，畜禽 水产 蔬菜 水果
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'reportIframe')))
    level = 0
    for i in all_num:
        name = '#tree农产品批发价格数据_'+str(i)+'_span'
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, name))).click()
        time.sleep(3)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'body > div.searchpanel '
                                                                               '> div.searchpanelright '
                                                                               '> div.searchtarget > iframe')))
        time.sleep(3)
        get_products(level)
        browser.switch_to.parent_frame()
        level += 1


def get_products(level):    # 获取分类下的小分类
    collection = db[col[level]]
    for j in range(2, point_num[level]):  # 一个j表示一行
        product = {}
        point = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#tab1 > table > tbody > '
                              'tr:nth-child('
                              + str(j) + ') > td.crosstabNodeMember > span'))).text

        time = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab1 > table > tbody >'
                                                                                ' tr:nth-child(1) > td:nth-child(2) > span'))).text
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab1 > table > tbody '
                                                                                '> tr:nth-child('
                                                                                 + str(j) + ') > td:nth-child(2) > span'))).text
        product[time] = price
        collection.update_one({'pro_name': point}, {'$set': {'time_price.' + time: price}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
        print(product)


if __name__ == '__main__':
    reptile()
    browser.close()
