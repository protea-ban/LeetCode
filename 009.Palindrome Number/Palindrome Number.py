class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = str(x)[::-1]

        return str(x) == ret


class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = x
        tmp = 0

        while x > 0:
            tmp = tmp * 10 + x % 10
            x //= 10

        return ret == tmp


if __name__ == '__main__':
    so = Solution2()
    x = 121
    # x = -121
    # x = 10
    ret = so.isPalindrome(x)
    print(ret)
