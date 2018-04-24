import requests
from requests import exceptions
import re
import time
import random
from multiprocessing.dummy import Pool
import csv
from parsel import Selector
from urllib import parse

def visit(url):
    heades = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]


    cookie=[
       '_T_WM=; SUB=_2A2533Gf_DeRhGeVI6VIQ9yjMyjuIHXVVPwm3rDV6PUJbkdAKLU3TkW1NTDSWVBZzR0NCfhqBJwRRFF1rNbLtlRDB; SUHB=04Wem2Ut8652WI; SCF=At3QwKArxK4xQxyfQ4-bvk6D1Oj7XCQDlJwXLkrHEiRHAvtEG9nhB6gpoKhKa4C01QNBqxIntg6HHLg5okplOug.; SSOLoginState=1524111279',
        '_T_WM=637c2cdc955836b1da2bdf7046794030; SUB=_2A2530QUDDeRhGeVI6VIQ9yjMyjuIHXVVPatLrDV6PUJbkdAKLVD3kW1NTDSWVF3TPGbvQo_R3DIKGEKHpKYmK3vD; SUHB=0P188WP42V8JPi; SCF=AqW46QkL-tNPFwwZFdNMJ2EdrLuAqOAeXSyaU3WDYOF6jgro9knMar32t__FDPUCF4I_Cm9gZVukWB499865_5A.; _WEIBO_UID=3620176017',
        '_T_WM=be1c3a29f969c7b3a895fb3a44f4d6b1; SUB=_2A2533GhbDeRhGeVI6VIQ9yjMyjuIHXVVPwgTrDV6PUJbkdAKLRXjkW1NTDSWVBRTGZq9wGpnUH-J377v8eJD_Ld0; SUHB=0oUYEja-0cIGsP; SCF=AmeDs4UdZ6yuhheJPqpW4F_ZoqUqqAZ4iSM9arwN7ATA_AwTCUJBGU2iaX4t7RXWJ7yWraAMZqroaQnVShdKSMc.; SSOLoginState=1524111371'
        '_T_WM=637c2cdc955836b1da2bdf7046794030; _WEIBO_UID=3620176017; _T_WL=1; SCF=At3QwKArxK4xQxyfQ4-bvk6D1Oj7XCQDlJwXLkrHEiRHpt58uvks7zYon6xzjsYsuCo0-pOJSutUeY_uF7yu-D0.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWbgBBpMNAZZJ.lTDkXslqk5JpX5K-hUgL.Foeceo5pS0q7eKM2dJLoI7f8qPijw-yLqPiXH8v-; SUB=_2A2533N4NDeRhGeVI6VIQ9yjMyjuIHXVVPuJFrDV6PUJbkdAKLUHekW1NTDSWVGVp9SbEIlk6DD4gI0YfiMzSYe17; SUHB=0KABGuTmNQnzKu; SSOLoginState=1524149853'
    ]


    headers = {
        'Cookie':random.choice(cookie),
        'User-Agent': random.choice(heades),
        'Connection':'keep-alive',
    }
    try:
        # time.sleep(2)
        result=requests.get(url,headers=headers)
        return result
    except exceptions.HTTPError as e:
        print(e.rason)


def get_fans_list(url):
    res = visit(url)
    parse_fans_list(res.text)


def parse_fans_list(res):

    # pattern = re.compile('<td.*?href="(.*?)">.*?</td>', re.S)
    # next_page = re.findall(pattern,res)

    response = Selector(text=res)
    user_list=response.xpath("//td[@valign='top'][1]/a/@href").extract()


    for each_user in user_list:

        if '/u' not in each_user:
            continue
        print('正在获取用户%s的个人信息' % each_user)

        get_eachuser_info(each_user)
        time.sleep(5)



def get_eachuser_info(url):
    url=url.replace('/u','')+'/info'
    content=visit(url)
    response = Selector(text=content.text)
    name=response.xpath("/ html / body / div[7] / text()[1]").extract_first()
    sex=response.xpath("/ html / body / div[7] / text()[2]").extract_first()
    address=response.xpath("/ html / body / div[7] / text()[3]").extract_first()
    tags=response.xpath("/ html / body / div[7] / a / text()").extract()

    if ':' in name:
        name=name.split(":")[1]

    if sex:
        sex=sex.split(":")[1]
    if address:
        address=address.split(":")[1]
    else:
        address='用户未填写'
    item=[]
    item.append(name)
    item.append(sex)
    item.append(address)
    if tags:
        item.append(tags)
    else:
        item.append('无标签')
    item_list.append(item)


def save(item_list):
    with open('烟民粉丝.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['昵称', '性别', '地址', '标签'])
        for each in item_list:
            if each[0]=='':
                continue
            writer.writerow(each)

if __name__=="__main__":
    item_list=[]
    urls=[]
    pool=Pool(4)
    url = ['https://weibo.cn/1873304560/fans?page={n}','https://weibo.cn/2678120877/fans?page={n}','https://weibo.cn/2232588561/fans?page={n}']
    for each_url in url:
        for i in range(1,21):
            urls.append(each_url.format(n=i))
    print(urls)

    try:
        pool.map(get_fans_list, urls)
    #     for each in urls:
    #         get_fans_list(each)
    #         time.sleep(10)
    # except:
    #     time.sleep(30)
    #     for each in urls:
    #         get_fans_list(each)
    #         time.sleep(20)
    finally:
        save(item_list)
    print("爬取完成")

