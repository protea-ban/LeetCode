class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 整数列表转成整数
        num = int(''.join([str(t) for t in digits]))
        # 加一
        num += 1
        # 将整数转成列表
        return [int(s) for s in str(num)]


if __name__ == '__main__':
    so = Solution()
    digits = [1,2,3]
    print(so.plusOne(digits))
