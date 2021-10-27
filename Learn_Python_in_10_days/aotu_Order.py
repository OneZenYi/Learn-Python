import json
from datetime import time

import requests
count = 0
url = 'https://v2r.proxypools.xyz'

host = url + '/api/v1/passport/auth/login'
data = {
    'email': '807002272@qq.com',
    'password': '_Zhangyi0'
}
r = requests.post(url=host, data=data)
cok = r.cookies
print(r.json())

count = 0
while (count < 20):
    host = url + '/api/v1/user/coupon/check'

    data = {
        'code': 'shenseven',
        'plan_id': '1'
    }
    r = requests.post(url=host, data=data,cookies=cok)
    print(r.json())
    print(r.status_code)
    #assert r.status_code == 200
    message = r.json()['message']
    if message == '优惠券已无可用次数':
        count = count + 1
    else:
        print(message)

host = url + '/api/v1/user/order/save'
data = {
    'cycle': 'month_price',
    'plan_id': 1,
    'coupon_code': 'qifei'
}
r = requests.post(url=host, data=data,cookies=cok)
trade_no = r.json()["data"]
print(trade_no)
print(r.json())
