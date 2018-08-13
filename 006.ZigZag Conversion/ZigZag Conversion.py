class Solution:

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 考虑到特殊情况，即行数小于等于1或者行数大于等于字符串长度
        if numRows <= 1 or numRows >= len(s):
            return s

        arr = [''] * numRows

        for i in range(len(s)):
            tmp = i % (numRows + numRows - 2)

            if tmp < numRows:
                arr[tmp] += s[i]
            else:
                arr[numRows + numRows - 2 - tmp] += s[i]

        return ''.join(arr)


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 4

    solution = Solution()

    ret = solution.convert(s, numRows)
    print(ret)


