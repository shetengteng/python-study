# coding:utf-8
import time
from MyWebDecorator import web_access

# 时间运行函数，返回时间
@web_access
def show_time(param):

    print(param)
    # 返回response body数据
    return time.ctime()

@web_access(ret_type="json")
def show_param(param):
    return param