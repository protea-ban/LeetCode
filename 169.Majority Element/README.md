# 169. 求众数

### 题目描述

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

### 示例

示例 1:

    输入: [3,2,3]
    输出: 3

示例 2:

    输入: [2,2,1,1,1,2,2]
    输出: 2

### 思路

#### 哈希计数法

遍历数组，将元素作为哈希表的键，元素出现的个数作为值，取数量超过 n/2 的元素输出。

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        length_nums = len(nums)

        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1

        for key, value in count_dict.items():
            if value > length_nums // 2:
                return key

        return

```

#### 排序计数法

对列表进行排序，然后遍历数组，对相同元素进行计数，一旦数量超过 n/2 即可返回该元素。

```python

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums = len(nums)
        nums.sort()
        count = 0
        current_item = nums[0]

        for item in nums:
            if current_item == item:
                count += 1
                if count > length_nums //2:
                    return item
            else:
                current_item = item
                count = 1
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)