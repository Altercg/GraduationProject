"""
添加超市和集市物价数据，使用这个函数
水产的集市价格和数据价格是图片
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pymongo

# 地址，不弹出窗口，设置browser
chrome_options = webdriver.ChromeOptions()  # 无界面模式
chrome_options.add_argument('--headless')
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities['pageLoadStrategy'] = "none"
browser = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
wait = WebDriverWait(browser, 100)

# 数据库准备操作
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.rept
col = {'猪肉': 'http://zdscxx.moa.gov.cn:8080/report/%E5%9B%BD%E5%86%85%E7%8C%AA%E8%82%89%E9%94%80%E5%94%AE%E4%BB%B7%E3%80%81%E8%B6%85%E5%B8%82%E4%BB%B7%E5%AF%B9%E6%AF%94%E6%83%85%E5%86%B5/index.html',
       '牛肉': 'http://zdscxx.moa.gov.cn:8080/report/%E6%9C%80%E6%96%B0%E5%9B%BD%E5%86%85%E7%89%9B%E4%BA%A7%E5%93%81%E4%BB%B7%E6%A0%BC%E8%B5%B0%E5%8A%BF/index.html',
       '羊肉': 'http://zdscxx.moa.gov.cn:8080/report/%E6%9C%80%E6%96%B0%E5%9B%BD%E5%86%85%E7%BE%8A%E4%BA%A7%E5%93%81%E4%BB%B7%E6%A0%BC%E8%B5%B0%E5%8A%BF/index.html',
       '白条鸡': 'http://zdscxx.moa.gov.cn:8080/report/%E9%B8%A1%E4%BA%A7%E5%93%81(%E9%B8%A1%E8%82%89)%E4%BB%B7%E6%A0%BC%E6%B3%A2%E5%8A%A8%E6%83%85%E5%86%B5/index.html',
       '鸡蛋': 'http://zdscxx.moa.gov.cn:8080/report/%E6%9C%80%E6%96%B0%E5%9B%BD%E5%86%85%E9%B8%A1%E8%9B%8B%E4%BB%B7%E6%A0%BC%E8%B5%B0%E5%8A%BF/index.html',
       '蔬菜集市': 'http://zdscxx.moa.gov.cn:8080/report/%E5%85%A8%E5%9B%BD%E4%B8%BB%E8%A6%81%E8%94%AC%E8%8F%9C%E9%9B%86%E5%B8%82%E4%BB%B7/index.html',
       '蔬菜超市': 'http://zdscxx.moa.gov.cn:8080/report/%E5%85%A8%E5%9B%BD%E4%B8%BB%E8%A6%81%E8%94%AC%E8%8F%9C%E8%B6%85%E5%B8%82%E4%BB%B7/index.html',
       '水果集市': 'http://zdscxx.moa.gov.cn:8080/report/%E5%85%A8%E5%9B%BD%E4%B8%BB%E8%A6%81%E6%B0%B4%E6%9E%9C%E9%9B%86%E5%B8%82%E4%BB%B7%E6%83%85%E5%86%B5/index.html',
       '水果超市': 'http://zdscxx.moa.gov.cn:8080/report/%E5%85%A8%E5%9B%BD%E4%B8%BB%E8%A6%81%E6%B0%B4%E6%9E%9C%E8%B6%85%E5%B8%82%E4%BB%B7%E6%83%85%E5%86%B5/index.html',
       '水产品': 'http://zdscxx.moa.gov.cn:8080/misportal/public/agricultureCategoryPage.jsp'}


def get_pig():    # 获取猪肉价格
    collection = db['meat']
    fair = {}
    supermarket = {}
    for i in range(2, 14):  # 一个j表示一行
        time = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_37.ml > span'))).text
        supermarket_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_43.mc_82531737 > span'))).text
        fair_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_45.mc_82531737 > span'))).text
        fair[time] = fair_price
        supermarket[time] = supermarket_price
    collection.update_one({'pro_name': '猪肉'}, {'$set': {'mell_price': fair}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
    collection.update_one({'pro_name': '猪肉'}, {'$set': {'super_price': supermarket}}, True)
    print(fair)
    print(supermarket)


def get_beef():    # 获取牛肉价格
    collection = db['meat']
    mell = {}
    super = {}
    for i in range(2, 14):  # 一个j表示一行
        time = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_35.ml > span'))).text

        mell_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_37.mc_82531737 > span'))).text

        super_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_39.mc_82531737 > span'))).text
        mell[time] = mell_price
        super[time] = super_price
    collection.update_one({'pro_name': '牛肉'}, {'$set': {'mell_price': mell}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
    collection.update_one({'pro_name': '牛肉'}, {'$set': {'super_price': super}}, True)
    print(mell)
    print(super)


def get_mutton():    # 获取羊肉价格
    collection = db['meat']
    mell = {}
    super = {}
    for i in range(2, 14):  # 一个j表示一行
        time = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_35.ml > span'))).text

        mell_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_37.mc_82531737 > span'))).text

        super_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_39.mc_82531737 > span'))).text
        mell[time] = mell_price
        super[time] = super_price
    collection.update_one({'pro_name': '羊肉'}, {'$set': {'mell_price': mell}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
    collection.update_one({'pro_name': '羊肉'}, {'$set': {'super_price': super}}, True)
    print(mell)
    print(super)


def get_chick():    # 获取鸡肉价格
    collection = db['meat']
    mell = {}
    super = {}
    for i in range(2, 14):  # 一个j表示一行
        time = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_41.ml > span'))).text

        mell_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_43.mc_82531737 > span'))).text

        super_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_49.mc_82531737 > span'))).text
        mell[time] = mell_price
        super[time] = super_price
    collection.update_one({'pro_name': '白条鸡'}, {'$set': {'mell_price': mell}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
    collection.update_one({'pro_name': '白条鸡'}, {'$set': {'super_price': super}}, True)
    print(mell)
    print(super)


def get_egg():    # 获取鸡蛋价格
    collection = db['meat']
    mell = {}
    super = {}
    for i in range(2, 14):  # 一个j表示一行
        time = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_35.ml > span'))).text

        mell_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_37.mc_82531737 > span'))).text

        super_price = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                              'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_39.mc_82531737 > span'))).text
        mell[time] = mell_price
        super[time] = super_price
    collection.update_one({'pro_name': '鸡蛋'}, {'$set': {'mell_price': mell}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
    collection.update_one({'pro_name': '鸡蛋'}, {'$set': {'super_price': super}}, True)
    print(mell)
    print(super)


def get_mell_veg():    # 获取蔬菜集市价格
    collection = db['vege']
    count = 0
    name_index = [28, 30, 32, 34, 36, 38, 40, 42]
    mell_index = [47, 49, 51, 53, 55, 57, 59, 61]
    for j in name_index:    # 选择特定的蔬菜
        mell = {}
        name = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) >'
                             ' table > tbody > tr:nth-child(1) > td.c_THIS_' + str(j) + '.xm > span'))).text
        if name == '萝卜':
            name = '白萝卜'
        for i in range(2, 14):  # i表示一列蔬菜，每列蔬菜的css不同
            time = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_45.ml > span'))).text

            mell_price = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                  'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_'
                                  + str(mell_index[count]) + '.mc_82531737 > span'))).text
            mell[time] = mell_price
        collection.update_one({'pro_name': name}, {'$set': {'mell_price': mell}}, True)       # 嵌套字典更新方式，最后一个参数，如不存在插入
        count += 1
        print(mell)


def get_super_veg():    # 获取蔬菜超市价格
    collection = db['vege']
    count = 0
    name_index = [28, 30, 32, 34, 36, 38, 40, 42]
    super_index = [47, 49, 51, 53, 55, 57, 59, 61]
    for j in name_index:  # 选择特定的蔬菜
        super = {}
        name = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) >'
                             ' table > tbody > tr:nth-child(1) > td.c_THIS_' + str(j) + '.xm > span'))).text
        if name == '萝卜':
            name = '白萝卜'
        for i in range(2, 14):  # i表示一列蔬菜，每列蔬菜的css不同
            time = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_45.ml > span'))).text

            super_price = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_'
                                  + str(super_index[count]) + '.mc_82531737 > span'))).text
            super[time] = super_price
        collection.update_one({'pro_name': name}, {'$set': {'super_price': super}}, True)  # 嵌套字典更新方式，最后一个参数，如不存在插入
        count += 1
    print(super)


def get_mell_frut():    # 获取水果集市价格
    collection = db['frut']
    count = 0
    name_index = [26, 28, 30, 32, 34]
    mell_index = [39, 41, 43, 45, 47]
    for j in name_index:  # 选择特定的蔬菜
        mell = {}
        name = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                             'table > tbody > tr:nth-child(1) > td.c_THIS_' + str(j) + '.xm > span'))).text
        if name == '苹果':
            name = '富士苹果'
        elif name == '梨':
            name = '鸭梨'
        for i in range(2, 14):  # i表示一列蔬菜，每列蔬菜的css不同
            time = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_37.ml > span'))).text

            super_price = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                  'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_'
                                   + str(mell_index[count]) + '.mc_82531737 > span'))).text
            mell[time] = super_price
        collection.update_one({'pro_name': name}, {'$set': {'mell_price': mell}}, True)  # 嵌套字典更新方式，最后一个参数，如不存在插入
        count += 1
        print(name, mell)


def get_super_frut():    # 获取水果超市价格
    collection = db['frut']
    count = 0
    name_index = [27, 29, 31, 33, 35]
    super_index = [40, 42, 44, 46, 48]
    for j in name_index:  # 选择特定的蔬菜
        super = {}
        name = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) >'
                             ' table > tbody > tr:nth-child(1) > td.c_THIS_' + str(j) + '.xm > span'))).text
        if name == '苹果':
            name = '富士苹果'
        elif name == '梨':
            name = '鸭梨'
        for i in range(2, 14):  # i表示一列蔬菜，每列蔬菜的css不同
            time = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_38.ml > span'))).text

            super_price = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td:nth-child(2) > '
                                 'table > tbody > tr:nth-child(' + str(i) + ') > td.c_THIS_'
                                  + str(super_index[count]) + '.mc_82531737 > span'))).text
            super[time] = super_price
        collection.update_one({'pro_name': name}, {'$set': {'super_price': super}}, True)  # 嵌套字典更新方式，最后一个参数，如不存在插入
        count += 1
        print(super)


if __name__ == '__main__':
    browser.get(col['猪肉'])
    get_pig()
    browser.get(col['牛肉'])  # 牛肉 ，羊肉，鸡蛋网页构造相同
    get_beef()
    browser.get(col['羊肉'])
    get_mutton()
    browser.get(col['白条鸡'])
    get_chick()
    browser.get(col['鸡蛋'])
    get_egg()
    browser.get(col['蔬菜集市'])
    get_mell_veg()
    browser.get(col['蔬菜超市'])
    get_super_veg()
    browser.get(col['水果集市'])
    get_mell_frut()
    browser.get(col['水果超市'])
    get_super_frut()
    browser.close()

