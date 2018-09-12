class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j]=True时表示长度为i的s与长度为j的p匹配成功
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # i=j=0时
        dp[0][0] = True
        # i=0,j>=1时
        for j in range(2, len(p) + 1):
            dp[0][j] = dp[0][j-2] and p[j - 1] == "*"

        # i>=1,j>=1时
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and \
                               (p[j-1] == '.' or p[j - 1] == s[i-1])
                else:
                    dp[i][j] = dp[i][j-2] or \
                               (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[i-1]))

        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    # s = "aa"
    # p = "a"

    # s = "aa"
    # p = "a*"

    # s = "ab"
    # p = ".*"

    # s = "aab"
    # p = "c*a*b"

    s = "mississippi"
    p = "mis*is*p*."
    ret = so.isMatch(s, p)
    print(ret)
