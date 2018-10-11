# 35.搜索插入位置

### 描述

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

### 示例

示例 1:

    输入: [1,3,5,6], 5
    输出: 2

示例 2:

    输入: [1,3,5,6], 2
    输出: 1

示例 3:

    输入: [1,3,5,6], 7
    输出: 4

示例 4:

    输入: [1,3,5,6], 0
    输出: 0

## 思路

对于不存在的情况， 我们只需要在数组里面找到最小的一个值大于 value 的 index ， 这个 index 就是我们可以插入的位置。 譬如 [1, 3, 5, 6] ， 查找 2 ， 我们知道 3 是最小的一个大于 2 的数值， 而 3 的 index 为 1 ， 所以我们需要在 1 这个位置插入 2 。 如果数组里面没有值大于 value ， 则插入到数组末尾。

```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

```

GitHub地址：https://github.com/protea-ban/LeetCode