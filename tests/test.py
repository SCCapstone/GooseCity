import requests
import json
import time
from lxml import html
host="http://127.0.0.1:8000"
print("Simulate user registration")
#Randomly generate username, email, phone, password.
phone=list(str(int(time.time()*10)))
phone[0]="1"
phone[1]="7"
phone[2]="8"
data={
    "username":str(int(time.time())),
    "email":str(int(time.time()))+"@163.com",
    "phonenum":"".join(phone),
    "password":str(int(time.time()))
}
print(data)
url=host+"/register/"
print(url)
time.sleep(1)
response_data=requests.post(url,data=data)
data=json.loads(response_data.content)
if data['flag']==1:
    print("Successfully registered")
else:
    print("registration failed")


session=requests.session()
print("Simulate login and get cookie")
url=host+"/login/"
user_info={
    "username":"1",
    "password":"1"
}
print(url)
time.sleep(1)
result=session.post(url,data=user_info)
print(result.cookies)
for item in result.cookies:
    print(item.name,item.value)
response_data=json.loads(result.content)
if response_data['flag']==1:
    print("login successful")

    urls=['/',"/search/","/user_person/","/change_info/","/done_s/"]
    for item in urls:
        item=host+item
        print(item)
        time.sleep(0.8)
        print(session.get(item).status_code)

    print("Get the shopping cart list information, modify the quantity, and pay by credit card")
    cart_url=host+"/user_person/"
    print(cart_url)
    time.sleep(1)
    tree=html.fromstring(session.get(cart_url).content)
    change_info=[]
    for item in tree.xpath("//table/tbody/tr"):
        info={
            "id":item.xpath("./td[1]/text()")[0],
            "name":item.xpath("./td[2]/text()")[0],
            "url":item.xpath("./td[3]/img/@src")[0],
            "desc": item.xpath("./td[4]/text()")[0],
            "price": item.xpath("./td[5]/span/text()")[0],
            "num": item.xpath("./td[6]/div/input[@type='text']/@value")[0],
        }
        print(info)
        info['delete']=host+item.xpath("./td[7]/a/@href")[0]
        info['card_id']=item.xpath("./td[7]/button/@data-id")[0]
        change_info.append(info)

    if len(change_info)==0:
        print("Shopping Cart is empty")
    else:
        print("Purchased product name：{},Product unit price：{}，Quantity:{}".format(change_info[0]['name'],
                                                          change_info[0]['price'],change_info[0]['num']))
        print("Change the number of products purchased to 8")
        data={
            "id":change_info[0]['card_id'],
            "num":8
        }
        url=host+"/change_count/"
        print(url)
        time.sleep(1)
        response=session.get(url,params=data)
        flag=json.loads(response.content)
        if flag['flag']==1:
            print("Successfully modified")

        print("Purchased product name：{},Product unit price：{}，Quantity:{}".format(change_info[0]['name'],
                                                  change_info[0]['price'], change_info[0]['num']))


        print("Modification of personal information")
        url=host+"/change_info/"
        print(url)
        phone = list(str(int(time.time() * 10)))
        phone[0] = "1"
        phone[1] = "7"
        phone[2] = "8"
        data={
            "username":1,
            "email":str(int(time.time()))+"@163.com",
            "phonenum":"".join(phone),
            "position":"Shenzhen City, Guangdong Province"
        }
        time.sleep(1)
        response=session.post(url,data=data)
        flag=json.loads(response.content)
        if flag['flag']==4:
            print("Name cannot be empty")
        elif flag['flag']==3:
            print("Address length is too long")
        elif flag['flag']==1:
            print("Successfully modified")
        else:
            print("fail to edit")



        print("Simulating a purchase...")
        data={
            "cartid":change_info[0]['card_id']
        }
        url=host+"/credit_buy/"
        print(url)
        time.sleep(1)
        response=session.get(url,params=data)
        data=json.loads(response.content)
        print(data)
        if data['flag']==1:
            print("successful purchase")
        elif data['flag']==2:
            print("Problem with address")
        else:
            print("Failed purchase")
        print("User test exit")
        url=host+"/logout/"
        print(url)
        time.sleep(1)
        session.get(url)
else:
    print("Simulated login failed")
backstage=['/backstage/welcome/','/backstage/product_add/']

data={
    "name":"n@163.com",
    "password":"1"
}
print("Simulate admin login")
url=host+"/backstage/login/"
print(url)
response=session.post(url,data=data)
flag=json.loads(response.content)
if flag['exist_count']==1:
    print("login successful")
    for item in backstage:
        item = host + item
        print(item)
        print(session.get(item).status_code)
else:
    print("Login failed")





