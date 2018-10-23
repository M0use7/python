"""__author__ = 余婷"""


class Lyric:
    def __init__(self, time, word):
        self.time = time
        self.word = word

    def __str__(self):
        return '%.2f %s' % (self.time, self.word)

    def __gt__(self, other):
        return self.time > other.time


class LyricAnalysis:
    """歌词解析类"""
    # 创建解析器对象的时候告诉我这个解析器是要解析哪首歌
    def __init__(self, song_name):
        # 保证一个歌词解析器对象对应一首歌
        self.song_name = song_name
        # 一首歌对应一个容器
        self.all_lyric = []
        # 解析歌词
        self.__collect_lyric()

    def __get_time_word(self, content):
        """提取歌词和时间"""
        contents = content.split(']')
        # 词
        word = contents[-1]
        for time in contents[:-1]:
            # 将时间转换秒
            times = time[1:].split(':')
            fen = float(times[0])
            miao = float(times[1])
            new_time = fen*60 + miao
            # 根据时间和词创建歌词对象
            lyric = Lyric(new_time, word)
            # 保存歌词对象
            self.all_lyric.append(lyric)

    def __collect_lyric(self):
        """将时间和词提取出来"""
        # 读歌词文件中的内容
        try:
            with open('./files/%s.txt' % self.song_name, 'r', encoding='utf-8') as f:
                # 一行一行的读
                line = f.readline()
                while line:
                    # 将每一行中的内容的词和时间弄出来
                    self.__get_time_word(line)
                    line = f.readline()
                # 排序
                self.all_lyric.sort(reverse=True)

                # for lyric in self.all_lyric:
                #     print(lyric)

        except FileNotFoundError:
            print('文件不存在')

    def get_word(self, time):
        """根据时间获取歌词"""
        for lyric in self.all_lyric:
            if lyric.time <= time:
                return lyric.word


an1 = LyricAnalysis('蓝莲花')
print(an1.get_word(120))


an2 = LyricAnalysis('十年')







if __name__ == '__main__':
    pass