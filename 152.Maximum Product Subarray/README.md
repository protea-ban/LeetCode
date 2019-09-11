# 152. 乘积最大子序列

### 题目描述

给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

### 示例

示例 1:

    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。

示例 2:

    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

### 思路

本题主要考虑使用动态规划的方法进行求解。

第一步，定义状态。设 DP[i] 为前 i 个数中的乘积最大子序列，其最大值应从 DP[i-1] 的最大值乘上 nums[i] 中取，这时需要考虑 nums[i] 的正负，若 nums[i] 为正，则 DP[i] 为 DP[i-1] 的最大值乘以 nums[i] ，否则为 DP[i-1] 的最大负值乘以 nums[i] 。所以，跟以往不同，本题的状态定义需要用到二维数组，即 DP[i][0] 存储前 i 个数中乘积正值最大子序列，DP[i][1] 存储前 i 个数中乘积负值最大子序列。

第二步，获得状态转移方程。
当然，本题的状态转移方程也是分为两种的。
```
if a[i] > 0:
    DP[i][0] = DP[i-1][0] * a[i]
    DP[i][1] = DP[i-1][1] * a[i]
else:
    DP[i][1] = DP[i-1][0] * a[i]
    DP[i][0] = DP[i-1][1] * a[i]
```

代码为：
```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res
        
```

上面代码运用了`滚动数组`的思想以降低空间复杂度，将原本 2\*len(nums) 大小的二维数组转成了 2\*2 大小的二维数组。当然该数组也可直接用变量直接代替，此时代码如下：

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        res, cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = cur_max * num, cur_min * num
            cur_min, cur_max = min(cur_max, cur_min, num), max(cur_max, cur_min, num)

            res = cur_max if cur_max > res else res
        
        return res
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)