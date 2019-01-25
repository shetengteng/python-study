# coding:utf-8
import time

# 时间运行函数，返回时间
def application(env,server_repsonse):
    # 遵从WSGI协议，可以从env中获取参数
    # env.get("PATH_INFO")
    # env.get("METHOD")

    status = "200 OK"
    headers = [
        ("Content-Type","text/plain")
    ]
    # WSGI要求返回status和headers
    server_repsonse(status,headers)
    # 返回response body数据
    return time.ctime()