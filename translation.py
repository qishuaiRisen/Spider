print('---------------------选择翻译网站-----------------------')
print('------------------1.有道翻译(双向译)--------------------')
print('------------------2.百度翻译(英译汉)--------------------')
print('------------------3.金山翻译(汉译英)--------------------')
choice=input('请选择翻译网站编号：')
import urllib.request
import json
import urllib.parse
import time
if choice=='1':
    while True:
        url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
        data={}
        content=input('请输入需要翻译的内容：\n')
        data['i']=content
        data['from']='AUTO'
        data['to']='AUTO'
        data['smartresult']='dict'
        data['client']='fanyideskweb'
        data['salt']='1510730310654'
        data['sign']='7c638ebdea58907ee45423c8d6740d83'
        data['doctype']='json'
        data['version']='2.1'
        data['keyfrom']='fanyi.web'
        data['action']='FY_BY_ENTER'
        data['typoResult']='false'
        data=urllib.parse.urlencode(data).encode('utf-8')
        respone=urllib.request.urlopen(url,data)
        html=respone.read().decode('utf-8')
        target=json.loads(html)
        print('翻译结果为：\n%s'%target['translateResult'][0][0]['tgt'])
        print('\n')
        time.sleep(5)
elif choice=='2':
    while True:
        content=input('请输入需要翻译的内容：\n')
        url='http://fanyi.baidu.com/v2transapi'
        data={}
        data['from']='en'
        data['to']='zh'
        data['query']=content
        data['transtype']='translang'
        data['simple_means_flag']='3'

        data=urllib.parse.urlencode(data).encode('utf-8')
        respone=urllib.request.urlopen(url,data)
        html=respone.read().decode('utf-8')
        target=json.loads(html)

        #print(html)
        print('翻译结果：\n%s'%(target['trans_result']['data'][0]['dst']))
        print('\n')
        time.sleep(5)
elif choice=='3':
    
    while True:
        url='http://fy.iciba.com/ajax.php?a=fy'
        data={}
        content=input('请输入要翻译的单词：')
        data['f']='auto'
        data['t']='auto'
        data['w']=content
        data=urllib.parse.urlencode(data).encode('utf-8')
        respone=urllib.request.urlopen(url,data)
        html=respone.read().decode('utf-8')
        target=json.loads(html)
        tgt=target['content']['out']
        #print(html)
        print('翻译结果为：\n%s'%tgt)
        print('\n')
        time.sleep(5)

    

