# 120. 三角形最小路径和

### 问题描述

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

### 示例

例如，给定三角形：
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

### 思路

首先考虑递归方法，即从根到节点计算出每条路径的和，最后求最小值，但这种方法时间复杂度较高，弃用。

考虑动态规划方法，进行从低到高的计算，首先进行状态定义，即走到第 i 行 j 列结点时的最短路径为 DP[i ,j] 。那么该值为其结点下面两个结点最短路径的最小值与 [i][j] 结点值的和，即转移方程为：`DP[i ,j] = min(DP[i+1 ,j], DP[i+1 ,j+1]) + triangle[i][j]` 。那么最后的结果肯定存储在第一层的节点当中。

写代码时，可以只用一维数组进行空间压缩，最后代码为：

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]

        return res[0]
        
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)