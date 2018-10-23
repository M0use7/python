"""__author__ = 余婷"""

class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show_time(self):
        print('%d:%d:%d' % (self.hour, self.minute, self.second))

class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show_date(self):
        print('%d年-%d月-%d日' % (self.year, self.month, self.day))