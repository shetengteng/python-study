# coding:utf-8
from  socket import *
from multiprocessing import *

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
            client = Process(target=handleClient,args=(newSocket,destAddr))
            client.start()
            # 已经向子进程中copy了一份（引用）
            newSocket.close()
    except Exception as e:
        print('error %s'%str(e))
    finally:
        tcp.close()

if __name__ == '__main__':
    main()