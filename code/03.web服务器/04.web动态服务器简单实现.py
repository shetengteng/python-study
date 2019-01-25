# coding=utf-8
from multiprocessing import *
# 导入正则
import re
import socket
import sys

# 静态文件根目录
HTML_ROOT_DIR="./html"
WSGI_ROOT_DIR="./wsgi-py"

class HTTPServer(object):
    """"""
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def bind(self,port):
        self.server_socket.bind(('',port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("[%s %s] 已经连接上了" % client_addr)
            p = Process(target=self.handle_conn, args=(client_socket, client_addr))
            p.start()
            client_socket.close()

    def handle_conn(self,client_socket,client_addr):
        # 接收数据
        request_data = client_socket.recv(1024);
        print("request data:",request_data)

        if(len(request_data)<=0):
            client_socket.close()
            return
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)

        request_start_line = request_lines[0]
        # 提取请求路径
        # 使用正则表达式进行划分
        # \w+ 多个字母开头 \s一个或者多个空格 /[^\s]*表示/后面非空格的多个值
        file_name = re.match(r"\w+\s+(/[^\s]*)\s",request_start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w+)\s+/[^\s]*\s",request_start_line.decode("utf-8")).group(1)

        if file_name.endswith(".py"):

            response_headers = "Server: My Server\r\n"
            def response(status, headers):
                nonlocal response_headers
                for header in headers:
                    response_headers += "%s: %s\r\n" % header


            # 表示获取文件名称 如：/index.py 获取下标从1开始到-3结束的位置
            # 使用__import__ 进行文件的调用 而该文件要满足WSGI标准，即含有一个application的调用方法
            try:

                m = __import__(file_name[1:-3])
            except Exception:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My Server\r\n"
                response_body = "the file is not found"
            else:
                # 该application方法含有2个参数，env 表示传递的参数 和server_response
                env = {
                    "PATH_INFO":file_name,
                    "METHOD":method
                }
                # 其中server_response 是传递的参数，用于传递headers信息给file_name的py文件使用
                # 使用属性方法实现
                # response_body = m.application(env, self.server_response)
                # 使用内部函数实现
                response_body = m.application(env, response)
                response_start_line="HTTP/1.1 200 OK\r\n"
        else:
            # 可以获得第一个/后面的值
            if "/" == file_name:
                # 判断默认路径
                file_name = "/index.html"
            # 打开文件,有可能打开的是图片，以二进制的方式读取
            try:
                file = open(HTML_ROOT_DIR+file_name,"rb")
            except IOError:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers="Server: My Server\r\n"
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
                response_headers="Server: My Server\r\n"
                response_body=file_data.decode("utf-8")

        response = response_start_line+response_headers+"\r\n"+response_body
        print("response data:",response)

        client_socket.send(bytes(response,"utf-8"))
        client_socket.close()

    def server_response(self,status,headers):

        response_headers = "Server: My Server\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

def main():
    # 在查找py的路径中，首先从wsgi路径上查找
    sys.path.insert(1,WSGI_ROOT_DIR)
    http_server = HTTPServer()
    http_server.bind(8088)
    http_server.start()

if __name__ == '__main__':
    main()