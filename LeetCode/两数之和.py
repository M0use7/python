"""__author__ = 唐宏进 """

class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        new_str = []
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    new_str.append(i)
                    new_str.append(j)
        return new_str
print(Solution.twoSum([2, 7, 11, 15],9))

