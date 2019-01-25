# coding:utf-8

import sys
import json

PAGE_STR="page"
HTML_ROOT_DIR="./html"
CONFIG_ROOT_DIR="./config"
PAGE_PY_DIR="./"+PAGE_STR

class Application(object):
    def __init__(self,urls):
        self.urls = urls

    def __call__(self,env,server_response):
        # 从env中获取path路径信息 使用get方法，如果没有则使用默认值 / 而不使用env["PATH_INFO"] 后者不存在会抛出异常
        path = env.get("PATH_INFO","/")
        if path == "/":
            path = "/index.html"

        # 访问静态文件 static
        if path.endswith(".html"):
            # 获取文件名称，从index 为 7开始截取
            # file_name = path[7:]
            # 打开文件读取内容
            try:
                file = open(HTML_ROOT_DIR+path,"rb")
            except IOError:
                return Application.not_found(server_response)
            else:
                file_data = file.read()
                file.close()
                return Application.ok_static(file_data,server_response)
        else:
            # for url,hander in self.urls:
                #("/ctime",show_time)
                # 在url中配置的path和对应的handler方法
            # 对于urls只用字典查询更加方便
            handler = self.urls.get(path)
            if handler is not None:
                module_name,method_name = handler.split(".")
                module_name = PAGE_STR+"."+module_name
                module = sys.modules.get(module_name)
                if module is None:
                    # 如果不加上fromlist=True,只会导入list目录
                    module = __import__(module_name,fromlist=True)
                return getattr(module,method_name)(env,server_response)

        return Application.not_found(server_response)

    # 文件未找到
    @staticmethod
    def not_found(server_response):
        status = "404 Not Found"
        headers = []
        server_response(status,headers)
        return "not found"

    # 返回静态文件
    @staticmethod
    def ok_static(file_data,server_response):
        status = "200 OK"
        headers = [("Server","myServer")]
        server_response(status,headers)
        return file_data.decode("utf-8")

# 将page-py的路径放入path中
sys.path.insert(1,PAGE_PY_DIR)
urls = json.load(open(CONFIG_ROOT_DIR+"/router.json",encoding="utf-8"))
app = Application(urls)
