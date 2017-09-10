# E:\Excise\python\t1\login.py

import requests
from bs4 import BeautifulSoup

url = "http://wlxy.hotwind.net/login.win"
UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"
 
header = { "User-Agent" : UA,
           "Referer": "http://wlxy.hotwind.net/login.win"
           }
 
v2ex_session = requests.Session()

 
postData = { 'name_com': '潘世瑞',
             'password_com': 'hotwind'
             }
 
loginReq = v2ex_session.post(url,
                  data = postData,
                  headers = header)
 
jar = loginReq.cookies

# print(jar["PHPSESSID"])

phpsession = jar["PHPSESSID"]

login_cookies = dict(PHPSESSID=phpsession)

print(login_cookies)

viewReq = v2ex_session.get('http://wlxy.hotwind.net/go.win?go=fee_web&primary=20323087&tid=1006546',
					cookies = login_cookies,
                  	headers = header)

jar1 = viewReq.cookies

# print(jar1)


for num in range(1,10):
	r1 = v2ex_session.get('http://wlxy.hotwind.net/template/green_hotwind/source/ajax/gocourse.win?tid=1006546&cid=1001554&pid=20323087',
		cookies = login_cookies,
		headers = header)
	print("request Num %d:%d"%(num,r1.status_code))
	# print(r1.headers)
