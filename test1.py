# -*- coding: UTF-8 -*-
'''import random
r=random.randint(1,9)
for i in range(3):
    n=int(input("猜个数字："))
    if n==r:
        print('猜对了')
        break
    if n>r:
        print('猜大了')
    else:
        print('猜小了')
'''

class box(object):
    def __init__(self,boxname,size,color):
        self.boxname = boxname
        self.size = size
        self.color =color
    def open(self,myself):
        print('-->用自己的myself,打开那个%s,%s的%s'  %  (myself.color,myself.size,myself.boxname))
        print('-->用类自己的self,打开那个%s,%s的%s'  %  (self.color,self.size,self.boxname))
    def close(self):
        print('-->关闭%s,谢谢' % self.boxname)


b = box('魔盒','15m','红色')

b.open(b)
b.close()
print(b.__dict__)

















