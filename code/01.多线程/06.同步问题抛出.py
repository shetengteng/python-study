# coding=utf-8

from threading import Thread
import time

g_num = 0;

def task1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('g_num--%s'%g_num)

def task2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('g_num--%s'%g_num)

if __name__ == '__main__':
    t = Thread(target=task1)
    t2 = Thread(target=task2)

    t.start()
    t2.start()

    print('g_num--%s'%g_num)