# 162.寻找峰值

### 描述

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

### 示例

示例 1:

    输入: nums = [1,2,3,1]
    输出: 2
    解释: 3 是峰值元素，你的函数应该返回其索引 2。

示例 2:

    输入: nums = [1,2,1,3,5,6,4]
    输出: 1 或 5 
    解释: 你的函数可以返回索引 1，其峰值元素为 2；
         或者返回索引 5， 其峰值元素为 6。

说明:

你的解法应该是 O(logN) 时间复杂度的。

## 思路
对于这题， 最简单地解法就是遍历数组， 只要找到第一个元素，大于两边就可以了，这种复杂度为 O(N) 。 但这题要求时间复杂度为 O(logN) ，所以我们通过二分来做。

首先我们找到中间节点 mid ， 如果大于两边返回当前 index 就可以了，如果左边的节点比 mid 大， 那么我们可以继续在左半区间查找， 这里面一定存在一个 peak ， 为什么这么说呢？假设此时的区间范围为 [0, mid -1] ， 因为 num[mid - 1] 一定大于 num[mid] 了， 如果 num[mid - 2] <= num[mid - 1] ， 那么 num[mid - 1] 就是一个 peak 。 如果 num[mid - 2] > num[mid - 1] ， 那么我们就继续在 [0, mid - 2] 区间查找， 因为 num[-1] 为负无穷， 所以最终我们绝对能在左半区间找到一个 peak 。 同理右半区间一样。

```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        start = mid = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return mid

```


GitHub地址：https://github.com/protea-ban/LeetCode