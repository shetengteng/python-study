# coding=utf-8
from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print('reader start pid%s ppid% '%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print('get from queue%s'%q.get(True))

def writer(q):
    print('writer start pid%s ppid% '%(os.getpid(),os.getppid()))
    for i in 'helloword':
        q.put(i)

if __name__=='__main__':
    print('%s start'%os.getpid())
    q = Manager().Queue() # 在进程池中如果要使用队列，那么需要使用Manager对象进行生成
    pool = Pool()
    # 使用阻塞的机制创建进程
    pool.apply(writer,(q,))
    pool.apply(reader,(q,))
    pool.close()
    pool.join()
    print('---end---pid:%s'%os.getpid())
