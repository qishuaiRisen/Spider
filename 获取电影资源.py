import requests
import random
from lxml import etree
import time
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
def get_one_page(url):
    headers={'User-Agent':random.choice(heades)}
    res=requests.get(url,headers=headers)
    parse_one_page(res.text)



def parse_one_page(content):
    selector=etree.HTML(content)
    data=selector.xpath("//div[@class='co_content8']//b/a/@href")
    eachmovie(data)
    #print(data)

def eachmovie(data):
    urll='http://www.dytt8.net'
    with open('电影资源.txt','a') as f:
        for each in data:
            try:
                om=requests.get(urll+each,headers={'User-Agent':random.choice(heades)})
            except:
                print('爬太快了，人家受不了了，等会儿吧！！！')
                time.sleep(20)
                om = requests.get(urll + each, headers={'User-Agent': random.choice(heades)})
            finally:
                om.encoding = 'gbk'
                result = parse_one_content(om.text)
                f.writelines(result + '\n')
                time.sleep(0.8)

        #print(urll+each)



def parse_one_content(om):
    selector = etree.HTML(om)
    data1=selector.xpath('//*[@id="Zoom"]//a[1]/@href')
    title=selector.xpath('//title/text()')
    data1.append(title)
    try:
        result=(str(data1[2])+'-------------------'+str(data1[1]))
    except:
        result = (str(data1[1]) + '-------------------' + str(data1[0]))
    print(result)
    return result

if __name__=='__main__':
    url='http://www.dytt8.net/html/gndy/dyzz/list_23_{n}.html'

    for i in range(10):
        try:
            get_one_page(url.format(n=i))
            time.sleep(10)
        except:
            print('爬太快了，人家受不了了，等会儿吧！！！')
            time.sleep(120)
            continue
