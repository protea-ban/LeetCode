# 4. 两个排序数组的中位数

### 问题描述
> There are two sorted arrays nums1 and nums2 of size m and n respectively.<br>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

### Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

### Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5
    
### 思路
1. 直接用python自带的函数，将两个列表相加，生成一个新列表。对新列表进行排序，然后求中位数。

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        resultList = nums1 + nums2
        resultList.sort()
        numLength = len(resultList)
        if numLength % 2 == 1:
            index = int((numLength + 1) / 2) - 1
            return resultList[index]
        else:
            index = int(numLength / 2) - 1
            return (resultList[index] + resultList[index + 1]) / 2
```

2. 由于两个列表自身有序，循环两个列表，将值较小的放入新列表中，把剩下的整个列表放到新列表中。则新列表有序，求中位数。

```python
class Solution:
    def findMedianSortedArrays0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = [0] * (len(nums1) + len(nums2))

        r_i, l_i, i = 0, 0, 0
        while (l_i < len(nums1)) and (r_i < len(nums2)):
            if nums1[l_i] < nums2[r_i]:
                nums3[i] = nums1[l_i]
                l_i = l_i + 1
            else:
                nums3[i] = nums2[r_i]
                r_i = r_i + 1

            i += 1

        if l_i != len(nums1):
            nums3[i:] = nums1[l_i:]
        else:
            nums3[i:] = nums2[r_i:]

        len_3 = len(nums3)
        if len_3 % 2 != 0:
            return float(nums3[(len_3 - 1) // 2])

        return (nums3[(len_3 - 1) // 2] + nums3[len_3 // 2]) / 2

```


### 结果思考
方法1要优于方法2，我认为可能是python提供的 sort方法的时间复杂度较低。

GitHub地址：https://github.com/protea-ban/LeetCode