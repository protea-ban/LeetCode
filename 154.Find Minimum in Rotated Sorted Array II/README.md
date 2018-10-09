# 154.寻找旋转排序数组中的最小值 II

### 描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

### 示例

示例 1：

    输入: [1,3,5]
    输出: 1

示例 2：

    输入: [2,2,2,0,1]
    输出: 0

## 思路

这题跟上题唯一的区别在于元素可能有重复， 我们仍然采用上面的方法， 只是需要处理 mid 与 start 相等这种额外情况。
- A[mid] > A[start]， 右半区间查找。
- A[mid] < A[start]， 左半区间查找。
- A[mid] = A[start]， 出现这种情况， 我们跳过 start， 重新查找， 譬如 [2,2,2,1]， A[mid] = A[start]都为 2，这时候我们跳过 start， 使用 [2,2,1] 继续查找。

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
            else:
                start += 1

        return min(nums[start], nums[stop])

```

GitHub地址：https://github.com/protea-ban/LeetCode