from threading import Thread
import time

g_num = 10

def task1():
    global  g_num
    for i in range(3):
        g_num +=1
        print('task1 g_num %s'%g_num)

def task2():
    global g_num
    print('task2 g_num %s'%g_num)

if __name__== '__main__':
    print('start--%s'%g_num)
    t1 = Thread(target=task1)
    t2 = Thread(target=task2)

    t1.start()
    time.sleep(2)
    t2.start()