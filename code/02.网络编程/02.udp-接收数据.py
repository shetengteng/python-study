# coding=utf-8

from socket import *

udp = socket(AF_INET,SOCK_DGRAM)
bindAddr = ('localhost',8088)

udp.bind(bindAddr)

# 接受数据 入参是接收的最大字节数
recvData = udp.recvfrom(1024)

print(recvData)

udp.close()