# -*- coding: UTF-8 -*-
from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('v2ex.html').read())

    print q('title').text()
    #>表示子元素，也就是div.inner下的a元素，<a href>
    #并且>要求找到的元素是相邻子元素，而空格只要求找到的是子元素或者是更内层的元素
    for each in q('div.inner>a').items():
        #找出标签栏
        if (each.attr.href.find('tab') > 0):
            #href是a标签的一个属性
            print(each.attr.href)

    #是id选择，.是class选择器
    for each in q('#Tabs>a').items():
        print each.attr.href

     #a[]的[]是正则表达式 要求href以/go开头，^+元素就是以某元素开头的意思
    for each in q('.cell>a[href^="/go/"]').items():
        print 3,each.attr.href
    for each in q('.cell a[href^="/go/"]').items():
        print 4,each.attr.href
    for each in q('span.item_title>a').items():
        print 5,each.html()
    for each in q('a>img.avatar').items():
        print 6,each.html()
