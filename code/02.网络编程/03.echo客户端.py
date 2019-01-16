# coding=utf-8
from socket import *

# 创建套接字
udp = socket(AF_INET,SOCK_DGRAM)

# ip 和 port
addr = ('localhost',8088)

while True:
    data = input('send data:')

    # 注意，这里发送需要进行转码操作，对于python3
    udp.sendto(data.encode(),addr)

    recvData = udp.recvfrom(1024)
    print(recvData)

udp.close()