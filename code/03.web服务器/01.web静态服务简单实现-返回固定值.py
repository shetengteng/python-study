# coding=utf-8
from socket import *
from multiprocessing import *

def handle_conn(client_socket,client_addr):

    # 接收数据
    request_data = client_socket.recv(1024);
    print("request data:",request_data)
    # 解析http数据报文

    # 提取请求方式
    # 提取请求路径

    # 返回响应的数据 http 响应格式
    """
        HTTP 1.1 200 OK\r\n
        \r\n
        hello world
    """
    # 构造响应数据
    response_start_line="HTTP/1.1 200 OK\r\n"
    response_headers="Server: My Server\r\n"
    response_body="hello world"
    response = response_start_line+response_headers+"\r\n"+response_body
    print("response data:",response)

    # 向客户端返回响应数据
    # client_socket.send(response.encode())
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()

if __name__ == '__main__':

    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 设置端口号
    server.bind(('', 8090))
    # 设置监听队列
    server.listen(128)

    while True:
        try:
            client_socket,client_addr = server.accept()
            # print("[%s %s] 已经连接上了"%(client_addr[0],client_addr[1]))
            # 等价于
            print("[%s %s] 已经连接上了"%client_addr)
            p = Process(target=handle_conn,args=(client_socket,client_addr))
            p.start()
            # 注意关闭client的socket 由于p进程已经收到client的socket，原先的关闭
            client_socket.close()
        except Exception as e:
            p.close()