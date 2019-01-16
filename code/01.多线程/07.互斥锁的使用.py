# coding=utf-8
from threading import Thread,Lock
import time

g_num = 0

mutex = Lock()

def task1():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if(mutexFlag):
            g_num += 1
            mutex.release()
    print('task1 g_num %s'%g_num)


def task2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if(mutexFlag):
            g_num += 1
            mutex.release()
    print('task2 g_num %s'%g_num)


if __name__ == '__main__':
    t = Thread(target=task1)
    t2 = Thread(target=task2)

    t.start()
    t2.start()

    print('main g_num %s'%g_num)