# 118. 杨辉三角

### 描述

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

![](http://pdg1wvjcw.bkt.clouddn.com/image/blog/Pascal.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

### 示例

    输入: 5
    输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

## 思路

要得到一个帕斯卡三角，只需要找到规律即可。
- 第 k 层有 k 个元素
- 每层第一个以及最后一个元素值为 1
- 对于第 k（k > 2） 层第 n（n > 1 && n < k） 个元素 A[k][n]， A[k][n] = A[k-1][n-1] + A[k-1][n]

```python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 对于第k（k > 2） 层第n（n > 1 && n < k） 个元素A[k][n]， A[k][n] = A[k-1][n-1] + A[k-1][n]
        res = []

        for i in range(numRows):
            temp = [0] * (i+1)
            res.append(temp)
            res[i][0] = 1
            res[i][len(res[i])-1] = 1

            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res
```

GitHub地址：https://github.com/protea-ban/LeetCode