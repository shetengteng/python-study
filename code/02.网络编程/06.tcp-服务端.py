# coding=utf-8
from socket import *

tcp = socket(AF_INET,SOCK_STREAM)
tcp.bind(('',8088))
#listen中的black表示已经建立链接和半链接的总数
#如果当前已建立链接数和半链接数以达到设定值,
# 那么新客户端就不会connect成功,而是等待服务器。直到有链接退出。
tcp.listen(3)
newSocket,clientAddr = tcp.accept()

recvData = newSocket.recv(1024)

print('recvData %s'%recvData.decode())

newSocket.send(('has recv:'+recvData.decode()).encode())
# 关闭连接
newSocket.close()
tcp.close()
