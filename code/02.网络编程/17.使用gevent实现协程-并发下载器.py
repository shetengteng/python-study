# coding=utf-8
from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()

def download(url):
    print('get %s'%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print("%s bytes received from %s"%(len(data),url))
    print("data---->%s"%data)

gevent.joinall([
    gevent.spawn(download,'https://cn.bing.com'),
    gevent.spawn(download,'https://www.baidu.com'),
    gevent.spawn(download,'https://www.sohu.com'),
])
