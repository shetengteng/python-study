#coding = utf-8
import threading
import time

# python2中
# from Queue import Queue

#python3中
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while(queue.qsize()<=100):
            for i in range(100):
                count +=1
                msg = self.name+'-p-'+str(count)
                queue.put(msg)
                print(msg)
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while(queue.qsize()>=100):
            for i in range(3):
                msg = self.name+'-c-'+queue.get()+'\n'
                print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    for i in range(100):
        queue.put('start-'+str(i))

    # 创建多个生产者
    for i in range(2):
        p = Producer()
        p.start()

    # 创建多个消费者
    for i in range(4):
        c = Consumer()
        c.start()

    print('------')