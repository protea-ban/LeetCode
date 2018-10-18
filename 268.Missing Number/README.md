# 268.缺失数字

### 描述

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

### 示例

示例 1:

    输入: [3,0,1]
    输出: 2

示例 2:

    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

## 思路

最直观的思路是对数据进行排序， 然后依次扫描， 便能找出漏掉的数字， 但是基于比较的排序算法的时间复杂度至少是 nlog(n) ， 不满足题目要求。

### 思路一：求和

一种可行的方法是对从 0 到 n 求和，然后对 nums 求和，两者之差就是缺失的数字，但是这种方式需要注意缺失的数是 0 的情况，即两者之和相等时可以认定为缺失的数是 0 。

```python
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0

        for i in range(0, len(nums)+1):
            sum1 += i

        for num in nums:
            sum2 += num

        if sum1 == sum2:
            return 0
        else:
            return sum1 - sum2
```

### 思路二：异或运算

异或运算的一个重要性质是，相同的数异或得 0 ，不同的数异或不为 0 ，且此性质可以推广到多个数异或的情形。 

本题的解法如下，首先将 0 到 n 这些数进行异或运算，然后对输入的数组进行异或运算，最后将两个结果进行异或运算，结果便是漏掉的数字， 因为其他数字在两个数组中都是成对出现的，异或运算会得到 0 。

```python
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(0, len(nums)+1):
            ret ^= i

        for num in nums:
            ret ^= num

        return ret
```

GitHub地址：https://github.com/protea-ban/LeetCode