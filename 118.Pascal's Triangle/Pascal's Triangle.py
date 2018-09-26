class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 对于第k（k > 2） 层第n（n > 1 && n < k） 个元素A[k][n]， A[k][n] = A[k-1][n-1] + A[k-1][n]
        res = []

        for i in range(numRows):
            temp = [0] * (i+1)
            res.append(temp)
            res[i][0] = 1
            res[i][len(res[i])-1] = 1

            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res


if __name__ == '__main__':
    so = Solution()
    numRows = 5
    print(so.generate(numRows))
