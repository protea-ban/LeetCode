# 153.寻找旋转排序数组中的最小值

### 描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

### 示例

示例 1:

    输入: [3,4,5,1,2]
    输出: 1

例 2:

    输入: [4,5,6,7,0,1,2]
    输出: 0

## 思路

这题要求在一个轮转了的排序数组里面找到最小值， 我们可以用二分法来做。

首先我们需要知道， 对于一个区间 A， 如果 A[start] < A[stop]， 那么该区间一定是有序的了。

假设在一个轮转的排序数组 A， 我们首先获取中间元素的值， A[mid]， mid = (start + stop) / 2。 因为数组没有重复元素， 那么就有两种情况：
- A[mid] > A[start]， 那么最小值一定在右半区间， 譬如 [4,5,6,7,0,1,2]， 中间元素为 7， 7 > 4， 最小元素一定在 [7,0,1,2] 这边， 于是我们继续在这个区间查找。
- A[mid] < A[start]， 那么最小值一定在左半区间， 譬如 [7,0,1,2,4,5,6]， 这件元素为 2， 2 < 7， 我们继续
在 [7,0,1,2] 这个区间查找。

```python
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return min(nums[0], nums[1])

        start = 0
        stop = len_nums - 1

        while start < stop - 1:
            if nums[start] < nums[stop]:
                return nums[start]

            mid = start + (stop - start) // 2

            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                stop = mid

        return min(nums[start], nums[stop])
```

GitHub地址：https://github.com/protea-ban/LeetCode