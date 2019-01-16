# coding=utf-8
from socket import *
from threading import Thread


def handleClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('recvData %s %s'%(str(destAddr),recvData))
        else:
            print('%s 任务已经关闭'%str(destAddr))
            break;
    newSocket.close()

def main():
    tcp = socket(AF_INET,SOCK_STREAM)
    tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp.bind(('localhost',8088))
    tcp.listen(5)

    try:
        print('----start----')
        while True:
            newSocket,destAddr = tcp.accept()
            print('---accpet---%s'%str(destAddr))
            # 开启一个新的进程进行处理
            client = Thread(target=handleClient,args=(newSocket,destAddr))
            client.start()
            #因为线程中共享这个套接字，如果关闭了会导致这个套接字不可用，
            #但是此时在线程中这个套接字可能还在收数据，因此不能关闭
            #newSocket.close()
    except Exception as e:
        print('error %s'%str(e))
    finally:
        tcp.close()

if __name__ == '__main__':
    main()