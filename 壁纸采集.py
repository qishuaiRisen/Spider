import requests
import re
import time
import random
import os
from lxml import etree
import urllib.request
heades=heades = [
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


headers={'User-Agent':random.choice(heades)}
def get_page_pic(url):
    res=requests.get(url,headers=headers)
    #print(res.text)
    res.encoding='gbk'
    parse_pic(res.text)

def parse_pic(res):
    pattern=re.compile('<li>.*?href="(.*?)".*?alt="(.*?)".*?</li>',re.S)
    result=re.findall(pattern,res)
    result=result[4:]
    print(result)
    get_pic(result)

def get_pic(result):
    url='http://pic.netbian.com{n}'
    for each_pic in result:
       get_pic_photo(url.format(n=each_pic[0]))

def get_pic_photo(pic_content):
    result1=requests.get(pic_content,headers=headers)
    result1.encoding='gbk'
    pattern=re.compile('<div.*?photo-pic">.*?title="(.*?)".*?img src="(.*?)".*?</a>.*?</div>',re.S)
    result2=re.findall(pattern,result1.text)
    get_pic_content_pic(result2)

def get_pic_content_pic(result2):
    url = 'http://pic.netbian.com{n}'

    for each in result2:
        #print(each)
        filename=each[1].split('/')[-1]
        print(filename)
        url=url.format(n=each[1])
        img_list=[]
        img_list.append(url)
        save_img(img_list)

def save_img(img_list):

    for each in img_list:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            # img = urllib.request.urlopen(each,headers)
            # f.write(img.read)
            img=requests.get(each,headers=headers)
            f.write(img.content)


if __name__=='__main__':
    url='http://pic.netbian.com'
    os.mkdir('壁纸')
    os.chdir('壁纸')
    get_page_pic(url)
    i=2
    while True:
        time.sleep(10)
        url1='http://pic.netbian.com/index_{n}.html'
        get_page_pic(url1.format(n=i))
        i+=1
    # for i in range(2,10):
    #     url1 = 'http://pic.netbian.com/index_{n}.html'
    #     url1 = url1.format(n=i)
    #     get_page_pic(url1)