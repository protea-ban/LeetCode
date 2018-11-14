## 905.按奇偶排序数组

### 问题描述

给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

### 示例

    输入：[3,1,2,4]
    输出：[2,4,3,1]
    输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

提示：

    1 <= A.length <= 5000
    0 <= A[i] <= 5000

## 思路

创建一个新的列表，深度拷贝要转换的数组。

设置两个下标，一个从 0 开始递增，用于存储偶数；一个从数组长度 - 1 开始递减，用于存储奇数。 

```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        import copy
        even_index = 0
        odd_index = len(A) - 1
        ret = copy.copy(A)

        for i in range(len(A)):
            if A[i] % 2 == 0:
                ret[even_index] = A[i]
                even_index += 1
            else:
                ret[odd_index] = A[i]
                odd_index -= 1

        return ret


if __name__ == '__main__':
    A = [3,1,2,4]
    so = Solution()
    print(so.sortArrayByParity(A))

```


GitHub地址：https://github.com/protea-ban/LeetCode