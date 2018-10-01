"""__author__ = 唐宏进 """


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if str(x)[-1] == '0':
            return int(str(x)[-2::-1])
        if x >= 0:
            if -2 ** 31 <= int(str(x)[::-1]) <= 2 ** 31 - 1:
                return int(str(x)[::-1])
            return 0
        else:
            if -2 ** 31 <= int('-'+str(x)[-1:0:-1]) <= 2 ** 31 - 1:
                return int('-'+str(x)[-1:0:-1])
            return 0


s1 = Solution()
print(s1.reverse(-123))

