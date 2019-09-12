class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1): dp[i][0] = i
        for j in range(m + 1): dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                dp[i-1][j] + 1,
                dp[i][j-1] + 1)

        return dp[n][m]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    sol = Solution()
    print(sol.minDistance(word1, word2))
