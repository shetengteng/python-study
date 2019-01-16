from multiprocessing import Pool
import time
import os

# 要在ubuntu下执行
# 执行函数，并返回一个值
def func1():
    print('pid %s ppid%s'%(os.getpid(),os.getppid()))
    for i in range(2):
        print('func1 run$s'%i)
        time.sleep(1)
    return 'param1'

def callBackFunc(args):
    print('callback pid%s'%os.getpid())
    print('params %s'%args)

if __name__=='__main__':
    pool = Pool(1)
    pool.apply_async(func=func1,callback=callBackFunc)
    time.sleep(4)
    print('main pid %s'%os.getpid())