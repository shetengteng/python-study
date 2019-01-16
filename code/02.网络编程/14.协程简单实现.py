import time

def A():
    while True:
        print("----A---")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print("----B---")
        # c.next() python2 支持
        c.__next__() # python3 支持
        time.sleep(0.5)

if __name__=='__main__':
    a = A()
    B(a)