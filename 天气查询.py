import requests
import json
import re
data=[]
def weather_search(city):
    url='https://www.sojson.com/open/api/weather/json.shtml?city='+city
    res=requests.get(url)
    if res.status_code==200:
        retest=json.loads(res.text)
        if retest['message']=='Check the parameters.':
            city=input('抱歉！您输入的城市有误，请检查后重新输入：')
            weather_search(city)
        else:
            parse(res)
    else:
        print('抱歉，此API接口停用了！')

def parse(res):
    r=json.loads(res.text)
    print(r['city']+'今日天气')
    q=r['data']
    print('湿度:'+q['shidu'])
    print('pm2.5:' + str(q['pm25']))
    print('空气质量:' + q['quality'])
    print('温度:' + q['wendu'])
    print('----------------分割线---------------------')
    b=input('是否显示未来七天的天气情况：')
    if b=='是':
        forecast(q)
    else:
        print('谢谢使用！再见！')
        return



def forecast(q):
    for each in q['forecast']:
        print('日期'+each['date'])
        print('高温' + each['high'])
        print('低温' + each['low'])
        print('天气' + each['type'])
        print('----------------分割线---------------------')




def main():
    city=input('请输入要查询的城市：')
    weather_search(city)

if __name__=='__main__':
    main()