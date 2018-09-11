# 9. 回文数

### 描述

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

### 示例

示例 1:

    输入: 121
    输出: true

示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？

## 思路

### 转成字符串解决

思路很简单，将整数转成字符串，反转后相比较即可。

```python
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = str(x)[::-1]

        return str(x) == ret
```

### 不转成字符串解决

题目中进阶是不转成字符串来解决这个问题。

其实也很简单，设置一个中间值，不断将整数除10取余，由中间值整合成倒数。

```python
class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = x
        tmp = 0

        while x > 0:
            tmp = tmp * 10 + x % 10
            x //= 10

        return ret == tmp
```

GitHub地址：https://github.com/protea-ban/LeetCode