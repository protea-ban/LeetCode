# 二分查找法
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l = 1
        r = x

        while l <= r:
            m = (l + r) // 2
            if m == x // m:
                return m
            elif m > x // m :
                r = m - 1
            else:
                l = m + 1
                res = m
        
        return res


# 牛顿迭代法
class Solution(object):
    def mySqrt(self, x):
        """

        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
