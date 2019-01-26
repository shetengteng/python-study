# coding:utf-8

import json

def web_access(func):
    def wrapped_func(env,server_repsonse):
        headers = [("Content-Type", "text/plain")]
        re = ""
        try:
            status = "200 OK"
            # WSGI要求返回status和headers
            server_repsonse(status, headers)
            # 返回response body数据
            param = env.get("QUERY_INFO")
            re = func(param)
        except Exception as e:
            status = "500 ERROR"
            server_repsonse(status,headers)
            re = str(e)
        return re
    return wrapped_func

def ret_json(func):
    def wrapped_func(*args,**kwargs):
        return json.dumps(func(*args,**kwargs))
    return wrapped_func