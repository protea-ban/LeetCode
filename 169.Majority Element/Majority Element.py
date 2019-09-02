# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 18:28
# @Author  : banshaohuan
# @Site    : 
# @File    : 169. Majority Element.py
# @Software: PyCharm
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        length_nums = len(nums)

        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1

        for key, value in count_dict.items():
            if value > length_nums // 2:
                return key

        return


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums = len(nums)
        nums.sort()
        count = 0
        current_item = nums[0]

        for item in nums:
            if current_item == item:
                count += 1
                if count > length_nums //2:
                    return item
            else:
                current_item = item
                count = 1

