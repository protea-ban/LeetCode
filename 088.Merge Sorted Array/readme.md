# 88.合并两个有序数组

### 描述

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

- 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
- 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

### 示例

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    
    输出: [1,2,2,3,5,6]

## 思路

两个数组都是有序的，此题类似于之前的有序链表合并，但是链表合并从小到大合并不涉及后续元素的移动，而数组不行。所以我们考虑从大到小进行比较合并。

nums1 和 nums2 都已经是排好序的数组， 我们只需要从后往前比较就可以了。

因为A有足够的空间容纳 nums1 + nums2 ， 我们使用游标 i 指向 m + n - 1 ， 也就是最大数值存放的地方，从后往前遍历 nums1 ， nums2 ，谁大就放到 i 这里，同时递减 i 。

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1

        while i >= 0:
            if j >= 0 and k >= 0:
                if nums1[j] > nums2[k]:
                    nums1[i] = nums1[j]
                    j -= 1
                else:
                    nums1[i] = nums2[k]
                    k -= 1
            elif j >= 0:
                nums1[i] = nums1[j]
                j -= 1
            elif k >= 0:
                nums1[i] = nums2[k]
                k -= 1

            i -= 1

```

GitHub地址：https://github.com/protea-ban/LeetCode