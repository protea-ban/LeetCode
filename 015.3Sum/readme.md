# 15. 三数之和


### 描述

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

### 示例

    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    
    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

## 思路

### 思路一

这种数值列表中有加减的题目，排序后可能会更加方便些。

固定两个数，将 target 设置为两个数之和的相反数，看 target 是否在列表中，若在，则为一个结果。

```python
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        # 数组题，其中有加减操作的，排序后会方便很多
        nums.sort()
        len_nums = len(nums)

        for i in range(len_nums - 1):
            for j in range(i+1, len_nums):
                # 固定下来两个数，如果另外一个数也在数组中，则为一个结果
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    a_ret = [nums[i], nums[j], -(nums[i]+nums[j])]
                    if a_ret not in ret:
                        ret.append(a_ret)

        return ret
```
但是这种方法有两层循环，果然报了 TLE（Time Limit Exceeded） 错误。

### 思路二

固定一个数，设置 target 为其他两个数之和的相反数，即 0 - 当前数，由两头向中间遍历数组，找到之和符合 target 的两个数即是一个结果。

```python
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()

        for i in range(0, len(nums)):
            # 若存在相同数，跳过以减少计算
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            start, end = i+1, len(nums)-1

            while start < end:
                # 头尾之和大于目标值，尾向前移一位
                if nums[start] + nums[end] > target:
                    end -= 1
                # 头尾之和小于目标值，头向后移一位
                elif nums[start] + nums[end] < target:
                    start += 1
                # 头尾之和等于目标值，是一个结果，添加进去
                # 头尾都移动一位
                else:
                    ret.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    # 若移动后有重复值，继续移动
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

        return ret

```

GitHub地址：https://github.com/protea-ban/LeetCode