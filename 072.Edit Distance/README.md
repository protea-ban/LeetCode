# 72. 编辑距离

### 题目描述

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

### 示例

示例 1:
```
输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```
示例 2:
```
输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

### 思路

本题用动态规划的方法来解。

第一步，定义状态。因为是两个单词，很容易发现仅仅一维是不能包含我们所有想要的信息，所以定义为二维数组 DP[i][j] ，表示 Word1 中的前 i 个字母组成的单词要想替换 Word2 中的前 j 个字母组成的单词的最少操作步骤。

第二步，设置状态转移方程。可以分为两种情况：
1. `w1[i] = w2[j]` 此时 `DP[i][j]=DP[i-1][j-1]` 。
2. `w1[i] != w2[j] `，此时可能做得操作有三种，即 `DP[i-1][j](insert)`, `DP[i][j-1](delete)`, `DP[i-1][j-1](replace)` ，所以 `DP[i][j]=min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1` 。

最后设置初始状态：一个单词为空，则另一个单词需要删除所有字母才能与之相匹配，所以操作数为单词字母的个数。

```python
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
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)