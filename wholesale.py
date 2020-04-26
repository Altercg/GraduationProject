"""
批发物价数据库为全空时，使用这个函数
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
db = client.rept    # 数据库的名称

all_num = [1, 9, 19, 59]    # 大类
class_num = [[2, 6], [10, 13], [20, 24, 26, 31, 36, 40, 43, 45, 51, 54, 57], [60, 63, 65, 68]]  # 小类
point_num = [[5, 4], [4, 7], [5, 3, 6, 6, 5, 4, 3, 7, 4, 4, 3], [4, 3, 4, 3]]   # 小类下的产品个数+2
col = ['meat', 'aqua', 'vege', 'frut']


def reptile():      # 获得大分类，畜禽 水产 蔬菜 水果
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'reportIframe')))  # 加载并且切换
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tree农产品批发价格数据_20_switch'))).click()  # 叶菜类结点可点击
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tree农产品批发价格数据_19_switch'))).click()  # 蔬菜结点可点击
    time.sleep(3)
    level = 0   # 记录到哪个大类了
    for i in all_num:
        name1 = '#tree农产品批发价格数据_'+str(i)+'_switch'
        tree = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, name1)))  # 大类结点可点击
        tree.click()    # 点击
        time.sleep(3)
        sm_level = 0    # 记录到大类的哪个小类了？
        for j in class_num[level]:
            name2 = '#tree农产品批发价格数据_'+str(j)+'_span'
            child = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, name2)))  # 小类结点可点击
            child.click()  # 点击
            classification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, name2))).text   # 获取小类的名字
            time.sleep(3)
            # 切换到右边子窗口
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'body > div.searchpanel '    
                                                                               '> div.searchpanelright '
                                                                               '> div.searchtarget > iframe')))
            get_products(level, sm_level, classification)
            sm_level += 1
            browser.switch_to.parent_frame()    # 回到上一个框架
        level += 1


def get_products(level, sm_level, classification):    # 获取产品
    collection = db[col[level]]  # 数据库下面的col[level]文件
    for p in range(2, point_num[level][sm_level]):  # 一个j表示一行
        product = {}
        # 获取农产品名称
        point = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#tab1 > table > tbody > '
                              'tr:nth-child('
                              + str(p) + ') > td.crosstabNodeMember > span'))).text
        product['pro_name'] = point
        # 存入小类
        product['classification'] = classification
        # 获取时间以及时间对应的价格
        for z in range(2, 14):
            times = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab1 > table > tbody >'
                                                                                ' tr:nth-child(1) > td:nth-child('
                                                                                + str(z) + ') > span'))).text
            price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab1 > table > tbody '
                                                                                '> tr:nth-child('
                                                                                 + str(p) + ') > td:nth-child('
                                                                                 + str(z) + ') > span'))).text
            product.setdefault('time_price', {})[times] = price     # 字典中的值通过设置成为另一个集合
        # 文件生成放入数据库
        collection.insert_one(product)
        print(product)


if __name__ == '__main__':
    reptile()
    browser.close()
