import threading

threadLocal = threading.local()

def handleName():
    # 获取当前线程中的参数
    print(threading.current_thread().name+'--name--'+threadLocal.name)

def task(name):
    threadLocal.name = name
    handleName()

if __name__ == '__main__':
    t1 = threading.Thread(target=task,args=('zhangsan',),name='task1')
    t2 = threading.Thread(target=task,args=('zhangsan2',),name='task2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

