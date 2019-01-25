# coding=utf-8
from socket import *
from multiprocessing import *
# 导入正则
import re

# 静态文件根目录
HTML_ROOT_DIR="./html"

def handle_conn(client_socket,client_addr):

    # 接收数据
    request_data = client_socket.recv(1024);
    print("request data:",request_data)

    if(len(request_data)<=0):
        client_socket.close()
        return

    # 解析http数据报文
    # 按照换行符进行分割
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)

    # 提取请求方式
    # 获取第一行
    # 'GET / HTTP/1.1'
    request_start_line = request_lines[0]
    # 提取请求路径
    # 使用正则表达式进行划分
    # \w+ 多个字母开头 \s一个或者多个空格 /[^\s]*表示/后面非空格的多个值
    file_name = re.match(r"\w+\s+(/[^\s]*)\s",request_start_line.decode("utf-8")).group(1)
    # 可以获得第一个/后面的值
    if "/" == file_name:
        # 判断默认路径
        file_name = "/index.html"

    # 打开文件,有可能打开的是图片，以二进制的方式读取
    try:
        file = open(HTML_ROOT_DIR+file_name,"rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_body="the file is not found"
    else:
        file_data = file.read()
        # 返回响应的数据 http 响应格式
        """
            HTTP 1.1 200 OK\r\n
            \r\n
            hello world
        """
        # 构造响应数据
        response_start_line="HTTP/1.1 200 OK\r\n"
        response_body=file_data.decode("utf-8")

    response_headers="Server: My Server\r\n"
    response = response_start_line+response_headers+"\r\n"+response_body
    print("response data:",response)

    # 向客户端返回响应数据
    # client_socket.send(response.encode())
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()

if __name__ == '__main__':

    server = socket(AF_INET, SOCK_STREAM)
    # 修改socket级别参数值reuseaddr，重用ip地址
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 设置端口号
    server.bind(('', 8090))
    # 设置监听队列
    server.listen(128)

    while True:
        client_socket,client_addr = server.accept()
        # print("[%s %s] 已经连接上了"%(client_addr[0],client_addr[1]))
        # 等价于
        print("[%s %s] 已经连接上了"%client_addr)
        p = Process(target=handle_conn,args=(client_socket,client_addr))
        p.start()
        # 注意关闭client的socket 由于p进程已经收到client的socket，原先的关闭
        client_socket.close()
