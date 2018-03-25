print('......密码安全性检查......')
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars='abcdefghijklmnopqrstuvwxyz'
charss='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='0123456789'
passwd=input('请输入要检查的密码:')
length=len(passwd)
secret=0
if length>16:
    passwd = input("您输入的密码超过16位，请重新输入：")
if length==0:
    print ('不可以用空密码')
elif 8<length<20:
    secret=2
elif length<=8:
    secret=1
else:
    print ('请输入16位以内的密码')

for each in passwd:
    if each in numbers:
        secret+=1
        break
for each in passwd:
    if each in chars:
        secret+=1
        break
for each in passwd:
    if each in symbols:
        secret+=1
        break
for each in passwd:
    if each in charss:
        secret+=1
        break

while 1:
    if secret==2:
        print ('您的密码安全等级为低级',secret)
        break
    elif secret==3:
        print('您的密码安全等级为中级',secret)
        break
    elif secret==5:
        print ('您的密码安全等级为高级',secret)
        break
    elif secret==6:
        print ('您的密码安全等级为顶级',secret)
        break
