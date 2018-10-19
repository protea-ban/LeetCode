class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        hasOne = False

        while n > 0:
            if n & 1:
                if hasOne:
                    return False
                else:
                    hasOne = True
            n >>= 1

        return hasOne


if __name__ == '__main__':
    so = Solution()
    print(so.isPowerOfTwo(218))
