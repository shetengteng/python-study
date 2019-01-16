# coding=utf-8
import select
from socket import *
import sys

tcp = socket(AF_INET,SOCK_STREAM)
tcp.bind(('localhost',8088))
tcp.listen(20)

running = True
# inputs = [tcp,sys.stdin] linux支持
inputs = [tcp]
print('---start---')
while True:
    # 参数1：检测这个列表中的套接字是否可以接收数据
    # 参数2：检测这个列表中的套接字是否可以发送数据
    # 参数3：检测这个列表中的套接字是否产生了异常
    readable,writeable,exceptional = select.select(inputs,[],[])

    for r_socket in readable:
        if(r_socket == tcp):
            # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,说明有新客户端连接进来了
            clientSocket,destAddr = tcp.accept()
            # 将客户端对象也加入到监听的列表中, 当客户端发送消息时 select 将触发
            print('---accpet---%s'%str(destAddr))
            inputs.append(clientSocket)
        elif r_socket == sys.stdin:
            # 表示键盘输入
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            # 进行读取操作
            data = r_socket.recv(1024)
            if len(data) > 0:
                print('recvData: %s'%data)
                r_socket.send(data)
            else:
                r_socket.close()
                inputs.remove(r_socket)