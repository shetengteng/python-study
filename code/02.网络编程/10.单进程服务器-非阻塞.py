# coding=utf-8
from socket import *

tcp=socket(AF_INET,SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp.bind(('localhost',8088))
tcp.listen(200)
# 设置为非阻塞，如果没有客户端connect 则会抛出异常
tcp.setblocking(False)

clientList = []

print('---accept---')
while True:
    try:
        clientSocket,destAddr = tcp.accept()
    except Exception as e:
        pass
    else:
        # 接收到连接后，放入连接池 否则始终是一个连接对象
        print('connect %s'%str(destAddr))
        clientSocket.setblocking(False)
        clientList.append((clientSocket,destAddr))

    deleteList = []
    for client,destAddr in clientList:
        try:
            recvData = client.recv(1024)
            if(len(recvData) > 0):
                print('recv data %s'%recvData)
            else:
                print('close %s'%str(destAddr))
                client.close()
                deleteList.append((client,destAddr))
        except Exception as e:
            pass

    for deleteItem in deleteList:
        clientList.remove(deleteItem)
