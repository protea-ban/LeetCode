# 338. 比特位计数

### 题目描述

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

### 示例

示例 1:

    输入: 2
    输出: [0,1,1]

示例 2:

    输入: 5
    输出: [0,1,1,2,1,2]

进阶:

- 给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描做到吗？
- 要求算法的空间复杂度为 O(n) 。
- 你能进一步完善解法吗？要求在 C++ 或任何其他语言中不使用任何内置函数（如 C++ 中的 \_\_builtin_popcount）来执行此操作。

### 思路

#### 位运算循环法

此题跟 [191 题](https://www.cnblogs.com/banshaohuan/p/9875736.html) 如出一辙，可以使用 191 的方法，循环求得每个数的位数。

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = []
        for i in range(num+1):
            bits.append(self.hammingWeight(i))

        return bits
    
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

#### 位运算迭代法

除了用位运算计算数值所含 1 的个数之外，还可以引入迭代的思想。

设 i 的个数为 count[i] ，那么 count[i] 的值肯定为比 i 所含 1 个数少一的值再加一(这个值不一定为 count[i-1] )，而比 i 所含 1 个数少一的数为 `i&(i-1)` 。并且有 `i&(i-1) < i < n` 的关系。所以肯定先有 count[i&(i-1)] 再有的 count[i] ， count[i] 的迭代式为：`count[i] = count[i&(i-1)] + 1` 。

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num+1)
        for i in range(1, num+1):
            bits[i] += bits[i & (i - 1)] + 1
        
        return bits
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)