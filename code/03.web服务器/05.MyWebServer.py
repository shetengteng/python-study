# coding=utf-8
import socket
import re
from urllib import parse

from MyWebFramework import app
from multiprocessing import Process

class HTTPServer(object):
    def __init__(self,app):
        self.app = app
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def bind(self,port):
        self.server_socket.bind(('',port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket,client_addr = self.server_socket.accept()
            print("%s %s connected"%client_addr)
            handle_client_process = Process(target=self.handle_conn,args=(client_socket,client_addr))
            handle_client_process.start()
            client_socket.close()

    # 处理数据请求
    def handle_conn(self,client_socket,client_addr):
        receive_data = client_socket.recv(1024)
        print("receive data:",receive_data)
        if len(receive_data) == 0:
            client_socket.close()
            return
        # 解析http协议,使用splitlines进行分割请求
        request_lines = receive_data.splitlines()
        for line in request_lines:
            print(line)
        # 解析请求头 GET / HTTP/1.1
        request_start_line = request_lines[0].decode("utf-8")
        method_name = re.match(r"(\w+)\s+/[^\s]*\s",request_start_line).group(1)
        file_url = re.match(r"\w+\s+(/[^\s]*)\s",request_start_line).group(1)
        url_info = parse.urlparse(file_url)
        file_name = url_info.path
        # 获取参数放入
        query_info = parse.parse_qs(url_info.query)

        env = {
            "PATH_INFO":file_name,
            "METHOD":method_name,
            "QUERY_INFO":query_info
        }

        response_header = "HTTP/1.1 ";
        def response(status, headers):
            nonlocal response_header
            response_header += status+"\r\n"
            for header in headers:
                response_header += "%s: %s\r\n" % header

        response_body = self.app(env,response)
        response = response_header + "\r\n" + response_body
        client_socket.send(response.encode("utf-8"))
        # client_socket.send(bytes(response,"utf-8"))
        client_socket.close()

def main():
    server = HTTPServer(app)
    server.bind(8088)
    server.start()

if __name__ == "__main__":
    main()