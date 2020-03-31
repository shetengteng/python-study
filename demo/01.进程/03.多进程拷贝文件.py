# coding=utf-8
from multiprocessing import Pool
import os


def copyFileTask():
    pass

def main():

    oldFileName = input('请输入文件夹的名称：')

    newFileName = oldFileName+'-副本'

    os.mkdir(newFileName)

    fileList = os.listdir(oldFileName)

    # 使用多进程的方式进拷贝
    pool = Pool(5)

    pool.apply_async(copyFileTask)


if __name__ == '__main__':
    main()