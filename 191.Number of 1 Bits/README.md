# 191.位1的个数

### 描述

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

### 示例

示例1 :

    输入: 11
    输出: 3
    解释: 整数 11 的二进制表示为 00000000000000000000000000001011
 

示例 2:

    输入: 128
    输出: 1
    解释: 整数 128 的二进制表示为 00000000000000000000000010000000

## 思路

### 方法一

设输入的数为 n ， 把 n 与 1 做二进制的与 (AND) 运算，即可判断它的最低位是否为 1 。 如果是的话，把计数变量加一。然后把 n 向右移动一位， 重复上述操作。 当 n 变为 0 时， 终止算法， 输出结果。

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            # n与上1，如果为1计数增加
            if n & 1 == 1:
                count += 1
            # n右移一位
            n >>= 1

        return count
```

### 方法二

利用位运算 `n & n - 1` 可以消除最后一位 1 的特性，不断消除 1 ，最后对操作次数计数即可。

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += 1
            n &= n - 1

        return count
```

GitHub地址：https://github.com/protea-ban/LeetCode