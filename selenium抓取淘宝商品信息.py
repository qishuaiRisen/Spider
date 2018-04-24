from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re
import pymongo
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser=webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait=WebDriverWait(browser,10)

MONGO_URL='localhost'
MONGO_DB='taobao'
MONGO_TABLE='product'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
def search(content):

    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    input.send_keys(content)
    button.click()
    total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
    get_product()
    return total.text



def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item ')))
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'dealnum':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()

        }
        print(product)
        save(product)

def next_page(page_number):
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
        next_button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        next_button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_product()
        print('正在翻页')
    except TimeoutException:
        next_page(page_number)



def save(product):
    try:
        if db[MONGO_TABLE].insert(product):
            print('保存成功')
    except Exception:
        print('保存失败')


def main():
    content=input('请输入要搜索的商品名：')
    try:
        page_number=search(content)
        page_number=int(re.compile("(\d+)",re.S).search(page_number).group(1))
        for i in range(2,page_number+1):
            next_page(i)
    finally:
        client.close()

if __name__=="__main__":
    main()