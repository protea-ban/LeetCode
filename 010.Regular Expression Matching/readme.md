# 10. 正则表达式匹配

### 描述

给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符。
    '*' 匹配零个或多个前面的元素。

匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

- s 可能为空，且只包含从 a-z 的小写字母。
- p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

### 示例

示例 1:

    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:

    输入:
    s = "aa"
    p = "a*"
    输出: true
    解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。

示例 3:

    输入:
    s = "ab"
    p = ".*"
    输出: true
    解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。

示例 4:

    输入:
    s = "aab"
    p = "c*a*b"
    输出: true
    解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。

示例 5:

    输入:
    s = "mississippi"
    p = "mis*is*p*."
    输出: false

## 思路

可以用**动态规划**的方法进行解决。

用 s[i] 表示字符串 s 的一个字符，用 p[j] 表示模式 p 中的一个字符。用 dp[i][j] = True 表示字符串 s 的前 i-1 个子串和模式 p 的前 j-1 个子串是匹配成功的。所以，遍历所有可能发生的情况，如果 dp[-1][-1] = True 则认为整个字符串匹配，所有情况分析如下：

1. i = 0; j = 0
    同时为空，认为匹配成功
2. i = 0; j = 1
    字符串 s 为空，模式 p 非空，认为匹配失败
3. i >= 1; j = 0
    字符串 s 不为空，模式 p 为空，认为匹配失败
4. i >= 0; j >= 2
    此时 dp[i][j] 可分解成 dp[i][j-2] 与 p[j-1] 且的情况。
5. i >= 1; j >= 1
    此时有 p[j-1] 是否为 '*' 的两种情况：
    - p[j-1] !='*'
        此时 dp[i][j] 可分解成 dp[i-1][j-1] 与 s[i-1] 和 p[j-1] 关系的且。
    - p[j-1] ='*'
        此时 dp[i][j] 可分解成 dp[i][j-2] 或上 dp[i-1][j] 与 s[i-1] 和 p[j-2] 关系的且。


```python
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

```


GitHub地址：https://github.com/protea-ban/LeetCode