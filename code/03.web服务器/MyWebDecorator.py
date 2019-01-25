# coding:utf-8

import json

def web_access(ret_type="text"):
    def wrapped_web_access(func):
        def wrapped_func(env,server_repsonse):
            headers = [("Content-Type", "text/plain")]
            if ret_type == "json":
                headers = [("Content-Type", "json/application")]
            elif ret_type == "text":
                pass
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

            if ret_type == "json":
                return json.dumps(re)
            else:
                return re

        return wrapped_func
    return wrapped_web_access

