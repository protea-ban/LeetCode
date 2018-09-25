# 66. 加一

### 描述

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

### 示例

示例 1:

    输入: [1,2,3]
    输出: [1,2,4]
    解释: 输入数组表示数字 123。

示例 2:

    输入: [4,3,2,1]
    输出: [4,3,2,2]
    解释: 输入数组表示数字 4321。

## 思路

其实很简单，将整数列表转成整数，加一后转回列表即可。

```python
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 整数列表转成整数
        num = int(''.join([str(t) for t in digits]))
        # 加一
        num += 1
        # 将整数转成列表
        return [int(s) for s in str(num)]
```


GitHub地址：https://github.com/protea-ban/LeetCode