# 300. 最长上升子序列

### 题目描述

给定一个无序的整数数组，找到其中最长上升子序列的长度。

### 示例
```
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
```
说明:

- 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
- 你算法的时间复杂度应该为 $O(n^2)$ 。

进阶: 你能将算法的时间复杂度降低到 O(nlogn) 吗?

### 思路

#### 动态规划法

第一步，定义状态。设 DP[i] 为第 i 个数时的最长上升子序列的长度。

第二步，设置状态转移方程。对于 DP[i] ，设 j<i 且 a[j]<a[i] ，则 DP[i] 的值为 DP[j] 中的最大值加上一（ a[i] 本身），即 `DP[i] = max{DP[j]} + 1` 。

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        res = 1
        dp = [1 for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            
            res = max(res, dp[i])
        
        return res
        
```

由于是双层循环，所以时间复杂度是 $O(n^2)$ 。


#### 二分查找法

本题用动态规划时的时间复杂度是 $O(n^2)$ ，而进阶中要求的将时间复杂度降到 O(nlogn) ，显然不能用动态规划了。

可以利用以空间换时间的思想来解决。第一步，设置一个用来放最长上升子序列的列表 LIS ；第二步，对 nums 进行遍历，将元素 nums[i] 放入 LIS 的可能情况为：对 LIS 进行二分查找，若 nums[i] > LIS[-1] ，则直接加入到 LIS 列表中，否则替换 LIS 中的元素；最后求得 LIS 的长度就是要返回的值。

由于只用了一层循环且二分查找的时间复杂度为 O(logn) ，所以该方法的时间复杂度为 O(nlogn) 。

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分查找 返回数组索引
        def binarySearch (arr, x): 

            if not arr or len(arr) == 0:
                return 0
  
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return low
        
        LIS = []
        for i in range(len(nums)):
            index = binarySearch(LIS, nums[i])
            if index == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[index] = nums[i]

        return len(LIS)
```


GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)