# coding=utf-8
import socket
import select

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 节省2msl时间,重复使用绑定的信息
tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcp.bind(('localhost',8088))
# 设置为被动
tcp.listen(1000)
# 创建一个epoll对象
epoll = select.epoll()

# 打印tcp对应的文件描述符
print('---server tcp file No --- %s'%tcp.fileno())

# 注册事件到epoll
# 如果tcp已经注册过，则会抛出异常
epoll.register(tcp.fileno(),select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

while True:
    # 获取连接的fd ，如果没有设置超时时间则进行阻塞
    epoll_list = epoll.poll()

    # 对事件进行判断
    for fd,events in epoll_list:
        if fd == tcp.fileno():
            conn,addr = tcp.accept()
            print('---accpet---%s'%str(addr))
            # 将conn和addr进行存储
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr
            # 在epoll中注册新的连接
            epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)

        elif events == select.EPOLLIN:
            # 读取信息
            recvData = connections[fd].recv(1024)
            if len(recvData) > 0:
                print('----recv data ---- %s'%(recvData))
            else:
                # 说明连接关闭，需要从epoll中移除
                epoll.unregister(fd)
                # tcp关闭该连接
                connections[fd].close()
                print('----close----%s'%str(addresses[fd]))
