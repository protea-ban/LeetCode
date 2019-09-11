# 322. 零钱兑换

### 题目描述

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

### 示例

示例 1:

    输入: coins = [1, 2, 5], amount = 11
    输出: 3 
    解释: 11 = 5 + 5 + 1

示例 2:

    输入: coins = [2], amount = 3
    输出: -1

说明:
你可以认为每种硬币的数量是无限的。

### 思路

用动态规划来解题。

第一步，定义状态， DP[i] 为兑换 i 元钱需要的最少硬币个数。

第二步，状态转移方程。`DP[i]=min{DP[i-coins[j]} + 1` 。DP[i - coins[j]] i 元钱减去 coins[j] 元钱后需要的最少硬币个数，然后加上 coins[j] 元钱就是 i 元钱需要的最少硬币个数。

```python
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

```


GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)