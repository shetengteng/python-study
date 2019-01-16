# coding=utf-8

import threading
from time import sleep,ctime

def task1():
    for i in range(3):
        print('task1 execute %s'%i)
        sleep(1)

def task2():
    for i in range(3):
        print('task2 execute %s'%i)
        sleep(1)

if __name__ == '__main__':
    print('---start---%s'%ctime())
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    print('---end---%s'%ctime())
    # 主线程会在所有的线程执行结束后结束，与java所不同

    while True:
        length = len(threading.enumerate())
        print('thread count:%s'%length)
        if length <=1 :
            break
        sleep(1)