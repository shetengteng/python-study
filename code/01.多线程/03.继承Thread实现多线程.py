import threading
import time

class MyThread(threading.Thread):
    # 重写run方法，线程在start的时候自动调用
    def run(self):
        for i in range(3):
            print('当前线程%s执行%s'%(self.name,i))
            time.sleep(1)

if __name__=='__main__':
    t = MyThread()
    t.start()

    t2 = MyThread()
    t2.start()