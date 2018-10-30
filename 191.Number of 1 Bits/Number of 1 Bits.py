class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            # n与上1，如果为1计数增加
            if n & 1 == 1:
                count += 1
            # n右移一位
            n >>= 1

        return count


if __name__ == '__main__':
    so = Solution()
    n = 128
    ret = so.hammingWeight(n)
    print(ret)
