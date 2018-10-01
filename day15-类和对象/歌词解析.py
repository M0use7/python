"""__author__ = 唐宏进 """


class Lyric:
    """歌词"""
    def __init__(self, time, word):
        self.time = time
        self.word = word

    def __str__(self):
        return '%.2f %s' % (self.time, self.word)
    def __gt__(self, other):
        return self.time > other.time


class LyricAnalyze:
    """歌词解析类"""
    def __init__(self, song_name):
        # 保证一个歌词解析器对象对应一首歌
        self.song_name = song_name
        # 一首歌对应一个容器
        self.all_lyric = []
        self.__get_lyric()

    def __get_time_word(self, content):
        """提取歌词和事件"""
        contents = content.split(']')
        # 词
        word = contents[-1]
        for time in contents[:-1]:
            # 将时间转换秒
            time = time[1:].split(':')
            fen = float(time[0])
            miao = float(time[1])
            new_time = fen*60 + miao

            # 根据时间和词创建歌词对象
            lyric = Lyric(new_time, word)
            # 保存歌词对象
            self.all_lyric.append(lyric)
    def __get_lyric(self):
        """将时间和词提取出来"""
        # 读取文件中的内容
        try:
            with open('./files/%s.txt'%self.song_name, 'r', encoding='utf-8') as f:
                    line = f.readline()
                    while line:
                        self.__get_time_word(line)
                        line = f.readline()

                    # 排序
                    self.all_lyric.sort(reverse=True)
        except FileNotFoundError:
            print('文件不存在！')

    def get_word(self, time):
        """根据时间获取歌词"""
        for lyric in self.all_lyric:
            if lyric.time <= time:
                return lyric.word


lyc = LyricAnalyze('蓝莲花')

print(lyc.get_word(24))