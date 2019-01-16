# coding=utf-8
from greenlet import greenlet
import time

def test1():
    while True:
        print('---test1---')
        gl2.switch()
        time.sleep(1)

def test2():
    while True:
        print('---test2---')
        gl1.switch()
        time.sleep(0.5)

gl1 = greenlet(test1)
gl2 = greenlet(test2)

if __name__== '__main__':
    # 先切换到第一个协程处理
    gl1.switch()