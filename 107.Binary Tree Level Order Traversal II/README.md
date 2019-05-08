# 107. 二叉树的层次遍历 II

### 描述

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

### 示例

例如，给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```
返回其自底向上的层次遍历为：

    [
      [15,7],
      [9,20],
      [3]
    ]

## 思路

本题相当于第 102 题的变形，而且本题给定的难度为`简单`,应该也是可以直接以第 102 题为参考做出来的([LeetCode102. 二叉树的层次遍历](https://www.cnblogs.com/banshaohuan/p/10824519.html))。

首先，可以来个投机取巧。观察本题的结果发现，其实本题的结果就是第 102 题结果的翻转。因此可以在第 102 题的代码上直接输入翻转后的列表：

```python
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if root is None:
                return

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)

        res = []
        dfs(root, 0, res)
        return res[::-1]
```

提交后给出的评价为：
> Runtime: 28 ms, faster than 53.21% of Python online submissions for Binary Tree Level Order Traversal II.

> Memory Usage: 12.7 MB, less than 5.52% of Python online submissions for Binary Tree Level Order Traversal II.

结果不是很理想，虽然不知道以切片方式翻转列表的内在原理，不过以结果来看该操作非常耗时。

那么，换一种思路，在进行深度优先遍历的时候直接将元素插入到合适的位置会怎么样呢？


通过分析，我们可以发现元素在列表中的下标（index）是与其所在层级（level）加一的负数（列表倒数），即 `index = -(level + 1)` ，所以有：
```python
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if root is None:
                return

            if len(res) <= level:
                res.insert(-(1+level), [])

            res[-(level+1)].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)

        res = []
        dfs(root, 0, res)
        return res

```

系统给出此种方法的评价为：

> Runtime: 20 ms, faster than 100.00% of Python online submissions for Binary Tree Level Order Traversal II.

> Memory Usage: 12.7 MB, less than 5.52% of Python online submissions for Binary Tree Level Order Traversal II.

GitHub 地址： https://github.com/protea-ban/LeetCode

![](https://img2018.cnblogs.com/blog/701977/201905/701977-20190501094902261-873549745.png)