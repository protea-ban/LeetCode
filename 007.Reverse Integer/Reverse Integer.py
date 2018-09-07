class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 记录x是正数还是负数
        sign = [1, -1][x < 0]

        # 反转后还需要加上正负
        ret = sign * int(str(abs(x))[::-1])

        # 如果溢出返回0
        return ret if -(2**31) < ret < 2**31 - 1 else 0


if __name__ == '__main__':
    so = Solution()
    ret = so.reverse(-12)
    print(ret)
