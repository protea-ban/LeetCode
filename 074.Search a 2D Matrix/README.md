# 74.搜索二维矩阵

### 描述

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

- 每行中的整数从左到右按升序排列。
- 每行的第一个整数大于前一行的最后一个整数。

### 示例

示例 1:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    输出: true

示例 2:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    输出: false

## 思路

对于这个给定的矩阵， 我们如果用 brute force 解法， 用两个嵌套循环， O(n^2) 便可以得到答案.但是我们需要注意的是这道题已经给定了这个矩阵的两个特性， 这两个特性对于提高我们算法的时间复杂度有很大帮助， 首先我们给出一个 O(n) 的解法， 也就是说我们可以固定住右上角的元素， 根据递增或者递减的规律， 我们可以判断这个给定的数值是否存在于这个矩阵当中.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        rowNumber = 0
        colNumber = len(matrix[0]) - 1

        while ((rowNumber < len(matrix)) and (colNumber >= 0)):
            if target < matrix[rowNumber][colNumber]:
                colNumber -= 1
            elif target > matrix[rowNumber][colNumber]:
                rowNumber += 1
            else:
                return True

        return False

```

GitHub地址：https://github.com/protea-ban/LeetCode