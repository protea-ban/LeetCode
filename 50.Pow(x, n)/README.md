# 50. Pow(x, n)

### 题目描述

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

### 示例

示例 1:

    输入: 2.00000, 10
    输出: 1024.00000

示例 2:

    输入: 2.10000, 3
    输出: 9.26100

示例 3:

    输入: 2.00000, -2
    输出: 0.25000
    解释: 2^-2 = 1/2^2 = 1/4 = 0.25($2^{-2}=1/2^2=1/4=0.25$)


### 思路

典型的分治算法题。

如果 n 为偶数，则计算 x 的 n/2 次方($x^{n/2}$)，然后结果相乘；如果 n 为奇数，则计算 x 的 (n-1/2) 次方($x^{(n-1)/2}$)，然后结果相乘后再乘以 x 。

 递归写法：
 
 ```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2:
            return x * self.myPow(x, n-1)

        return self.myPow(x*x, n//2)
```

非递归写法：
 
n 的二进制位为 1 ，需要累积相乘，否则是需要 x 自身相乘，n 右移一位，相当于 n 除以 2。

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1

        return pow

```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)