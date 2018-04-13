import requests
import json
import csv
def get_info(start_url,headers):
    result=requests.get(start_url,headers=headers)
    #print(result)
    if result.status_code==200:

        parse_info(result)

def parse_info(result):
    result=json.loads(result.content)
    if 'stocks' in result.keys():
        result=result['stocks']
        with open('xueqiudata.csv', 'w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['股票代码', '股票名称','当前价','涨跌幅','市值','市盈率'])
            for res in result:
                item=[]
                item.append(res.get('code'))
                item.append(res.get('name'))
                item.append(res.get('current'))
                item.append(res.get('change'))
                item.append(res.get('marketcapital'))
                item.append(res.get('pettm'))
                to_save(item,writer)
            print('爬取完成')

def to_save(item,writer):

    writer.writerow(item)




if __name__=='__main__':
    start_url = 'https://xueqiu.com/stock/cata/stocklist.json?page=1&size=100&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=1523591781538'
    headers={

    'Cookie':'s=fy113vej64; xq_a_token=229a3a53d49b5d0078125899e528279b0e54b5fe; xq_r_token=8a43eb9046efe1c0a8437476082dc9aac6db2626; u=461523587527637; device_id=0550c2088bfa4ee80cecf8248ef17aed; __utmt=1; __utma=1.1175708765.1523587528.1523587528.1523587528.1; __utmb=1.3.10.1523587528; __utmc=1; __utmz=1.1523587528.1.1.utmcsr=github.com|utmccn=(referral)|utmcmd=referral|utmcct=/OpenSauce-IO/interview/blob/master/questions/crawler.md; Hm_lvt_1db88642e346389874251b5a1eded6e3=1523587528,1523587781,1523589426; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1523589426',
    'Referer':'https://xueqiu.com/hq',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
    }

    get_info(start_url,headers)