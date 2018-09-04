# 1. 两数之和

### 描述

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


### 示例

    给定 nums = [2, 7, 11, 15], target = 9
    
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
 

## 思路

建立一个键为数值在 nums 中的序号，值为 nums 列表的数值的字典，对 nums 列表进行遍历，对于其中的每一数，得到其数与目标值的差值，在字典中寻找该差值，若找到该差值且该差值的键与之前的减数的键不同，且因为默认只有一种答案，所以减数的键和差值的键就是要返回的结果。

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dd = {nums[i]: i for i in range(n)}
        for i in range(n - 1):
            cha = target - nums[i]
            if cha in dd and i != dd[cha]:
                return [i, dd[cha]]
        return 'null'
```


GitHub地址：https://github.com/protea-ban/LeetCode