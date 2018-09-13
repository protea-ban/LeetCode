# 11. 盛最多水的容器

### 描述

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

![](http://pdg1wvjcw.bkt.clouddn.com/question_11.jpg)

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


### 示例

    输入: [1,8,6,2,5,4,8,3,7]
    输出: 49

## 思路

### 思路一

此题其实就是在求矩形面积，最简单暴力的方法就是双循环记录最大面积。

```python
class Solution0:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 初始面积设为0
        max_area = 0

        len_h = len(height)

        for i in range(len_h):
            for j in range(i, len_h):
                area_w = j - i
                area_h = min(height[i], height[j])
                new_area = area_w * area_h
                if new_area > max_area:
                    max_area = new_area

        return max_area
```
提交后报 TLE(Time Limit Exceeded) 错误，想想也没毛病，毕竟双循环在数量比较大的时候会出现这种问题。

### 思路二

矩形的面积就是宽乘以高，可以在宽最大化的情况下寻找最高的可能来实现面积最大。

所以，设置两个指针指向两端，逐渐向中间靠拢，寻找面积最大的可能。

```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 初始化最大面积
        max_area = 0

        # 初始化两头的指针
        left = 0
        right = len(height) - 1

        # 循环
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

```

GitHub地址：https://github.com/protea-ban/LeetCode