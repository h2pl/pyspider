# -*- coding: UTF-8 -*-

#http请求模块
import re

import requests

#HTML解析的工具包
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get("http://www.qiushibaike.com").content
    soup = BeautifulSoup(content, "html.parser")

    #class:content是根据html中我们想要的格式来进行匹配的
    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip() + '\n'

def demo_string():

    #类似Java，有增加额外方法
    stra = 'hello'
    print stra.capitalize()
    print stra.replace('he', 'ha')
    strb = '   \n  \rget \r \n   '
    print(1, strb.rstrip())
    print(2 , strb.lstrip())
    print(3, stra.startswith('h'))
    print(4, stra.endswith('h'))
    print(5, stra + strb)
    print(6, stra, len(stra), len(strb))

    print(7, '-'.join(['a','b','c']))

    strc = 'hello world'
    print(strc.split(' '))
    print(strc.find('a'))

def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 1, 1 + 2, 5 / 2.0, 5 * 2, 5 - 2
    print(2, True, not True, False)

    print(1 << 2, 88 >> 2)
    print(5 | 3, 2 & 4, 6 ^ 2)

def demo_function():
    max([1])
    len('1')
    range(1,10,2)
    print(dir(list))

    x = 2
    #如果x是个对象，可以用eval直接使用，可以用于写java语言
    print(6,eval('x*2 + 5 + 3'))

    print(chr(66), ord('a'))
    print(divmod(11, 3))

#控制流略

#list

def demo_list():
    list1 = [1, 'a', 5.0, 23, 76]
    list2 = [1, 'a', 5.0, 23, 1212]
    print(list1)
    for i in list1:
        print(i)
    print(list1.extend(list2))
    print(1 in list2)

    #操作符重载，两个相连
    list2 = list2 + list1
    print(list2)

    list2.insert(0, 'dasdasda')
    list2.pop(1)
    print(list2)

    list2.sort()
    print(list2)

    list2.reverse()
    print(list2.count(1))

    #tuple不可变
    t = (1, 2, 3)
    print(t)


def add(a, b):
    return a + b


def demo_dict():
    dict = {'a' : 1, 'b': "a"}
    print(dict)
    print(dict.keys(), dict.values())
    for key, value in dict.items():
        print(key, value)
    for key in dict.keys():
        print(key)
    print(dict.has_key(1))
    a = add
    print(a(1, 2))


class User:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return "i am a guest" + self.name + str(self.uid)


class Admin(User):
    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return "i am a guest" + self.name + str(self.uid) + self.group


def demo_object():
    user = User('jim', 1)
    print(user)

    admin = Admin('xiangyu', 1, 'a')
    print(admin)


def demo_exception():
    try:
        print(2/1)
        raise Exception("dasdas")
    except Exception as e:
        print(e)
    finally:
        print('final')


#随机数略

#正则表达式

def demo_regex():
    str = 'abc123def12gh15'
    #\d是digit数字 \w是字符串和数字 \s是空格 +代表匹配多次
    #[]就是用来把一个式子包起来，和数学的（）类似
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    p3 = re.compile('[\d]')
    print(1, p1.findall(str))
    print(2, p2.findall(str))
    print(3, p3.findall(str))

    str = 'a@163.com,b@google.com,c@qq.com,d@163.com'

    #.是正则表达式中的特殊字符，需要用\转义
    p4 = re.compile('[\w]+@[163|qq|google]+\.com')
    print(p4.findall(str))

    str = '<html><h>title</h><body>content</body></html>'

    #  ^<说明首字符必须是<
    p5 = re.compile('<h>[^<]+</h>')
    print(p5.findall(str))
    p5 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print(p5.findall(str))

    str = 'xx2016-08-20zzz,xx2016-7-20zzz'
    p6 = re.compile('\d{4}-\d{2}-\d{2}')
    print(p6.findall(str))

if __name__ == '__main__':
    #qiushibaike()
    #demo_string()
    #demo_operation()
    #demo_function()
    #demo_list()
    #demo_dict()
    #demo_object()
    #demo_exception()

    demo_regex()
