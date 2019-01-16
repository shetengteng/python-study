# coding=utf-8
from socket import *
from time import ctime

port = 21567
bufferSize = 1024

udp = socket(AF_INET,SOCK_DGRAM)
udp.bind(('',port))

print('wait msg')
while True:
    data,raddr =  udp.recvfrom(bufferSize)
    print('recv %s %s'%(raddr,data.decode()))
