# 231.2的幂

### 描述

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

### 示例

示例 1:

    输入: 1
    输出: true
    解释: 2^0 = 1

示例 2:

    输入: 16
    输出: true
    解释: 2^4 = 16

示例 3:

    输入: 218
    输出: false

## 思路

首先，可以肯定的是负数一定不是 2 的幂次方。

2 的整数次幂对应的二进制数只含有 0 个或者 1 个 1 ， 所以我们要做的就是判断输入的数的二进制表达形式里是否符合这一条件。 


>"&" :按位与运算符：参与运算的两个值,如果两个相应位都为 1 ,则该位的结果为 1 ,否则为 0 。



>">>" :右移动运算符：把 ">>" 左边的运算数的各二进位全部右移若干位， >> 右边的数字指定了移动的位数。

```python
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        hasOne = False

        while n > 0:
            if n & 1:
                if hasOne:
                    return False
                else:
                    hasOne = True
            n >>= 1

        return hasOne
```

GitHub地址：https://github.com/protea-ban/LeetCode