# coding=utf-8
from socket import *

tcp = socket(AF_INET,SOCK_STREAM)

tcp.connect(('localhost',8088))

data = input('send data')

tcp.send(data.encode())

recvData = tcp.recv(1024)
print('recv data %s'%recvData.decode())

tcp.close()