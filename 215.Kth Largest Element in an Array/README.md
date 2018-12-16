# 215. 数组中的第K个最大元素

### 问题描述

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

### 示例

示例 1:

	输入: [3,2,1,5,6,4] 和 k = 2
	输出: 5

示例 2:

	输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
	输出: 4


### 思路

从大到小排序，返回第 k-1 个元素。

```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        # print(nums[k-1])
        return nums[k-1]


if __name__ == '__main__':
    so = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4

    # nums = [3,2,1,5,6,4]
    # k = 2

    so.findKthLargest(nums, k)
```

GitHub地址：https://github.com/protea-ban/LeetCode