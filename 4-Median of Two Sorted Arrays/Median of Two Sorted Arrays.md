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
2. 由于两个列表自身有序，循环两个列表，将值较小的放入新列表中，把剩下的整个列表放到新列表中。则新列表有序，求中位数。
### 结果思考
方法1要优于方法2，我认为可能是python提供的`sort`方法的时间复杂度较低。