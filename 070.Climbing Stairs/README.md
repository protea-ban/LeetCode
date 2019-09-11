# 70. 爬楼梯

### 题目描述

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

### 示例

示例 1：

    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶

示例 2：

    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶

### 思路

典型的动态规划题。我们设到第 n 阶一共有 f(n) 种走法，那么 f(n) = f(n-1) + f(n-2) 。因为要么从第 n-1 个阶梯上迈一步，要么从第 n-2 个阶梯上迈两步。

可见该题变成了斐波拉契数列的形式，因此，代码为：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        
        return y
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)