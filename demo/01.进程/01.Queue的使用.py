# coding=utf-8
from multiprocessing import Process,Queue
import os,time,random

# 注意：在windows情况下执行不成功，在ubuntu执行成功

# 写数据进程
def write(q):
    for v in ['a','b','c']:
        print('put %s to queue...'%v)
        q.put(v)
        time.sleep(1)

# 读数据进程
def read(q):
    while True:
        if not q.empty():
            v = q.get(True)
            print('get %s from queue'%v)
            time.sleep(random.random())
        else:
            # 读取完queue中的进程就结束
            break

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动进程
    pw.start()
    # 等待pw进程写结束
    pw.join()
    # 启动读进程
    pr.start()
    pr.join()
    print('---end---')