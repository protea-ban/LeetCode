# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 11:15
# @Author  : banshaohuan
# @Site    : 
# @File    : Valid Anagram.py
# @Software: PyCharm
# 排序法 O(NlogN)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}

        for item_s in s:
            if item_s not in s_dict:
                s_dict[item_s] = 1
            else:
                s_dict[item_s] += 1

        for item_t in t:
            if item_t not in t_dict:
                t_dict[item_t] = 1
            else:
                t_dict[item_t] += 1

        return s_dict == t_dict


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))