# coding=utf-8
from socket import *

dest = ('<broadcast>',21567)

udp = socket(AF_INET,SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
udp.setsockopt(SOL_SOCKET, SO_BROADCAST,1)

while True:
    data = input('>')
    if not data:
        break
    print("sending -> %s"%data)
    # 广播的方式发送到所有的服务端上
    udp.sendto(data.encode(), dest)
