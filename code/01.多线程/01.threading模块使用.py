# coding=utf-8

import threading
import time

def task(tId):
    print('当前线程编号：%s开始执行\n'%tId)
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        # 创建一个线程
        t = threading.Thread(target= task,args=(i,))
        # 执行这个线程
        t.start()