# -*- encoding=UTF-8 -*-

import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world"'
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    strb = '   \n\rhello nowcoder \r\n  '
    print 0, strb
    print 1, strb.lstrip()
    print 2, strb.rstrip(), "xx"
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(stra), len(strb), len(strc)
    print 7, 'x'.join(['a', 'b', 'c'])  # StringBuilder
    print 8, strc.split(' ')
    print 9, strc.find('llo')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 1, 1 + 2, 5 / 2.0, 5 * 2, 5 - 2
    print 2, True, not True, not False
    print 3, 1 << 2, 88 >> 2  # 0x11111
    print 4, 1 < 2, 5 < 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3  # 0x101 0x011
    x = 3
    y = 5.0
    print x, y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2), abs(7)
    print 4, range(1, 10, 2)
    # print 5, '\n'.join(dir(list))
    x = 2
    print x + 3
    print 6, eval('x*2+4')
    print 7, chr(66), ord('a')
    print 8, divmod(11, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'
    while score < 100:
        print score
        score += 10
        if score > 80:
            break

    # for (int i = 0; i < 10; ++i)
    for i in range(0, 10):
        if i == 0:
            pass
        if i == 3:
            continue
        if i < 5:
            print i * i
        if i == 7:
            break

            # print i


def demo_list():
    lista = [1, 2, 3]  # vector<int> ArrayList<Integer>
    print 1, lista
    # print dir(list)
    listb = ['a', 1, 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in lista, 'b' in lista
    lista = lista + listb
    print lista
    listb.insert(0, 'wwwwwww')
    print listb
    listb.pop(1)
    print listb
    listb.sort()
    print listb
    print listb[1], listb[2]
    print listb * 2
    print [0] * 10  # memset
    listb.append('xxx')
    print listb
    listb.reverse()
    print listb
    t = (1, 1, 3)  # pair<int, xxx>
    print t
    print t.count(1), len(t)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9, 'a': 'b'}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    for key, value in dicta.items():
        print 3, key, value
    for key in dicta.keys():
        print 4, key
    print 5, dicta.has_key(1), dicta.has_key(11)

    dictb = {'+': add, '-': sub}
    print 6, dictb['+'](1, 2)
    print 7, dictb.get('-')(6, 2)

    print 8, dictb
    del dictb['+']
    print 9, dictb

    dictb.pop('-')
    print 10, dictb

    dictb['x'] = 'y'
    print dictb
    # Map.put(key, value)


def demo_set():
    lista = (1, 2, 3)
    seta = set(lista)
    print 1, seta
    setb = set((2, 3, 4))
    print 2, seta.intersection(setb)
    print 3, seta & setb
    print 4, seta | setb, seta.union(setb)
    print 5, seta - setb, setb - seta
    seta.add('xxx')
    print 6, seta
    print 7, len(seta)
    print seta.isdisjoint(set(('a', 'b')))
    print 8, 1 in seta


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)
        # toString()


class Guest(User):
    def __repr__(self):
        return 'im guest ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    '''
    def __repr__(self):
        return 'im admin ' + self.name + ' ' + str(self.uid) + ' ' + self.group
    '''


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 2, 'g1')
    else:
        return Guest('g1', 3)


def demo_object():
    user1 = User('jim', 1)
    print user1
    guest1 = Guest('lily', 2)
    print guest1
    admin1 = Admin('xiangyu', 3, 'nowcoder')
    print admin1
    print create_user('ADMIN')


def demo_exception():
    try:
        print 2 / 1
        # print 2/0
        raise Exception('Raise Error', 'XXXX')
    except Exception as e:
        print 'error', e
    finally:
        print 'clean up'


def demo_random():
    # random.seed(1)
    # x = prex * 100007 % xxxx
    # prex = x

    for i in range(0, 5):
        print 1, random.randint(0, 100)
    print 2, int(random.random() * 100)
    print 3, random.choice(range(0, 100, 5))
    print 4, random.sample(range(0, 100, 10), 5)

    lista = [1, 2, 3, 4, 5]
    random.shuffle(lista)
    print lista

def demo_regex():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)

    str = 'axxx@163.com,bcc@google.com,c@qq.com,d@qq.com,e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str)
    p4 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print 5, p4.findall(str)

    str = 'xx2016-08-20zzz,xx2016-8-20zzz'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print p5.findall(str)


if __name__ == '__main__':
    # qiushibaike()
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    # print 'hello world'
    # demo_object()
    # demo_exception()
    #demo_random()
    demo_regex()
