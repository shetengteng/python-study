#coding=utf-8
from socket import *
import random
import time

connNum = int(input("请输入要链接服务器的次数(例如1000):"))
g_socketList = []
for i in range(connNum):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8088))
    g_socketList.append(s)
    print(i)

while True:
    for s in g_socketList:
        msg = str(random.randint(0,100)).encode()
        print('--send---%s'%msg)
        s.send(msg)

    # 用来测试用
    time.sleep(1)