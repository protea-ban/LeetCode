# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 17:30
# @Author  : banshaohuan
# @Site    : 
# @File    : Pow(x, n).py
# @Software: PyCharm
class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2:
            return x * self.myPow(x, n-1)

        return self.myPow(x*x, n//2)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1

        return pow
