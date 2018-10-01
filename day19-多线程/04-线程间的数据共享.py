"""__author__ = 唐宏进 """
from threading import Thread,Lock
import time
"""
模拟多个人对同一个账号进行操作

同步锁(RLock)和互斥锁(Lock)
"""

class Account:
    """账号类"""
    def __init__(self, balance):
        # 余额
        self.balance = balance
        # 创建锁对象
        self.lock = Lock()

    # 存钱的过程：读出原来的余额，确定钱一系列操作，将原来的余额加上存的数额产生最新的余额保存
    def save_money(self, amount):
        """存钱"""
        print('开始存钱')
        # 加锁
        self.lock.acquire()
        # 获取原来的余额
        old_amount = self.balance
        # 模拟时间消耗
        time.sleep(5)
        self.balance = old_amount + amount
        print('存钱成功！最新余额:',self.balance)
        # 解锁
        self.lock.release()

    def take_money(self, amount):
        """取钱"""
        print('开始取钱')
        # 加锁
        self.lock.acquire()

        old_amount = self.balance
        if amount > old_amount:
            print('余额不足！')
            return
        time.sleep(5)
        self.balance = self.balance - amount
        print('取钱成功！最新余额:',self.balance)
        # 解锁
        self.lock.release()

    def show_balance(self):
        print('当前余额为:',self.balance)


# 创建账号
# p1 = Account(1000)
# p1.save_money(200)
# p1.take_money(100)
# p1.show_balance()

"""
当多个线程同时对一个数据进行操作的时候，可能会出现数据混乱的问题
"""
p1 = Account(1000)
t1 = Thread(target=p1.save_money, args=(200,))
t2 = Thread(target=p1.save_money, args=(100,))
t3 = Thread(target=p1.take_money, args=(500,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
p1.show_balance()

