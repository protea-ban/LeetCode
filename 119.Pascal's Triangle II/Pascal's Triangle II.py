class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex + 1)

        for i in range(rowIndex + 1):
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j-1]

        return res


if __name__ == '__main__':
    so = Solution()
    rowIndex = 4
    print(so.getRow(rowIndex))
