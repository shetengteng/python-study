# coding=utf-8
from socket import *
# tcp 连接
tcp = socket(AF_INET,SOCK_STREAM)
# 可以重复绑定接口使用 ，在连接释放时tcp4次挥手，需要2msl的时间，
# 在此时间内如果要建立tcp连接，原先的端口要释放，否则等待建立
# 此处设置后，服务器先进行tcp4次挥手，可以将本端口立即重新使用，不需要等待2msl
tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

tcp.bind(('localhost',8088))
# 表示接受5个请求，含有全连接和半连接个数（在linux下该配置已linux的内核配置为主）
tcp.listen(5)

while True:
    print('--- server start ---')
    newSocket,destAddr = tcp.accept()
    print('---主进程处理数据---地址：%s'%str(destAddr))
    try:
        while True:
            recvData = newSocket.recv(1024)
            if(len(recvData) > 0):
                print('接收到数据 %s %s'%(str(destAddr),recvData))
            else:
                print('连接已关闭 %s'%str(destAddr))
                break

    except Exception as e:
        print('error:%s'%str(e))
    finally:
        newSocket.close()

tcp.close()