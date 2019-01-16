# coding=utf-8
from socket import *
from threading import Thread

udp = None
ip = ''
port = ''

def recvData():
    while True:
       data,recvAddr = udp.recvfrom(1024)
       # 添加 \r 可以将内容从头打印
       print('\r>> %s %s'%(str(recvAddr),data.decode()))

def sendData():
    while True:
        data = input('<<')
        udp.sendto(data.encode('gb2312'),(ip,port))

def main():

    global ip
    global port
    global udp

    ip = input('ip:')
    port = int(input('port:'))
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(('172.20.10.4',8088));
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)
    tr.start()
    ts.start()
    tr.join()
    ts.join()

if __name__ == '__main__':
    main()