#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:BanShaohuan
@file: Two Sum.py
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dd = {nums[i]: i for i in range(n)}
        for i in range(n - 1):
            cha = target - nums[i]
            if cha in dd and i != dd[cha]:
                return [i, dd[cha]]
        return 'null'

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)