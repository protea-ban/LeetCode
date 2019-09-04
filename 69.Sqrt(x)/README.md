# 69. x 的平方根

### 题目描述

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

### 示例

示例 1:

    输入: 4
    输出: 2

示例 2:

    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842..., 
         由于返回类型是整数，小数部分将被舍去。

### 思路

#### 二分查找法

因为 $y=x^2$ 是递增的，所以可以使用二分查找。

先是将 l 设为 0 ，r 设为 y ，mid = (l+r)/2 ，观察 mid 的平方与 y 的关系，如果 ${mid}^2 > y$ ，令 r=mid 进行下一轮，否则令 l=mid 进行下一轮。

```python
# 二分查找法
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l = 1
        r = x

        while l <= r:
            m = (l + r) // 2
            if m == x // m:
                return m
            elif m > x // m :
                r = m - 1
            else:
                l = m + 1
                res = m
        
        return res
```

#### 牛顿迭代法

该方法是数学思维上求平方根的一种方法，详情可参考[百度百科](https://baike.baidu.com/item/%E7%89%9B%E9%A1%BF%E8%BF%AD%E4%BB%A3%E6%B3%95)。

```python
# 牛顿迭代法
class Solution(object):
    def mySqrt(self, x):
        """

        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r

```

而编程语言内置方法多用另一种类似算法，详情可参考[Beyond3D - Origin of Quake3's Fast InvSqrt()](https://www.beyond3d.com/content/articles/8/)。

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)