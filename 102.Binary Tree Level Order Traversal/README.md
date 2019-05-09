# 102. 二叉树的层次遍历


### 描述

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

### 示例

例如，给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：

    [
      [3],
      [9,20],
      [15,7]
    ]

## 思路

关于树的问题基本上都是用递归来解决的，此题也是需要考虑递归。

对树，常使用的查找方法有深度优先查找和广度优先查找，在此使用 DFS ，因为它的代码易于理解。

层次遍历的核心在于需要设置一个层数变量，在进行 DFS 的时候将节点放入相应层数的列表中。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
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
        return res
```

GitHub 地址： https://github.com/protea-ban/LeetCode

![](https://img2018.cnblogs.com/blog/701977/201905/701977-20190501094902261-873549745.png)