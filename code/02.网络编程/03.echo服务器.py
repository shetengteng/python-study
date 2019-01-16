# coding = utf-8
from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

udp.bind(('localhost',8088))

num = 1
while True:
    # 接收对方数据并返还
    recvData = udp.recvfrom(1024)
    # 接收的示一个元祖数据，第一个是结果，第二个是发送方的ip和port
    udp.sendto(recvData[0],recvData[1])
    print('callback %d %s'%(num,recvData[0].decode()))
    num += 1

udp.close()
