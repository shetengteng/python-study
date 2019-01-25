import sys
import time
import gevent
# 注意使用socket要是gevent封装的
from gevent import socket, monkey

monkey.patch_all()

def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("receive data%s"%data)
        conn.send(data)

tcp = socket.socket()
tcp.bind(('localhost',8088))
tcp.listen(10)
print("---start---")
while True:
    clientConn,addr = tcp.accept()
    gevent.spawn(handle_request,clientConn)
