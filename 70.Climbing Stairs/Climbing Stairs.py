class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        
        return y