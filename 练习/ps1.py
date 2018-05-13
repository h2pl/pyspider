#coding=utf-8
import requests
payload = {'username' : 'xx', 'password' : 'xx'}
s = requests.session()
print(s.get("http://127.0.0.1:8080/user/6")).content
#登录请求
r = s.post('http://127.0.0.1:8080/login', data=payload)
print(s.get("http://127.0.0.1:8080/user/6")).content
#根据登录后的请求获取cookie
print(s.get("http://127.0.0.1:8080/user/6", cookies={"ticket":"xxx"})).content




