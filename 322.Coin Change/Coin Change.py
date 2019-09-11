class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        
        return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    coins = [1]
    amount = 1
    sol = Solution()
    res = sol.coinChange(coins, amount)
    print(res)
