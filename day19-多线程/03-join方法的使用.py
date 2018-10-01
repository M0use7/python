"""__author__ = 唐宏进 """
from threading import Thread
from random import randint
import datetime
import time

# 在两个子线程中下载两个电影，在主线程中去统计两个电影下载的总时间
"""
如果希望某个线程结束后才执行某个操作，就用那个线程调用join方法
"""
class DownloadThread(Thread):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def run(self):
        print(self.file + '开始下载:', datetime.datetime.now())
        time.sleep(randint(5, 10))
        print(self.file + '下载结束:', datetime.datetime.now())

t1 = DownloadThread('恐怖游轮')
t2 = DownloadThread('美丽人生')

start = time.time()

t1.start()
t2.start()

# 系统t1和t2中的代码都结束才执行下面的代码
t1.join() # 这句代码后面的代码在t1对应的线程结束后才执行
t2.join()
end = time.time()
print(end-start)


