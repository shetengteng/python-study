# coding = utf-8
# 由于是共享的引用变量，不是线程安全的

from threading import Thread
import time

def task1(nums):
    nums.append(33)
    print('---task1---',nums)

def task2(nums):
    time.sleep(1)
    print('---task2---',nums)

if __name__ == '__main__':

    g_num = [1,2,3]
    t = Thread(target=task1,args=(g_num,))
    t2 = Thread(target=task2,args=(g_num,))
    t.start()
    t2.start()
