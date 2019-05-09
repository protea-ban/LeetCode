# 103. 二叉树的锯齿形层次遍历

### 描述

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

### 示例

例如，给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```
返回锯齿形层次遍历如下：

    [
      [3],
      [20,9],
      [15,7]
    ]

## 思路

本题相当于第 102 题的变形，应该也是可以直接以第 102 题为参考做出来的([LeetCode102. 二叉树的层次遍历](https://www.cnblogs.com/banshaohuan/p/10824519.html))。

首先，最容易想到的方法就是按照第 102 题的算法得到遍历列表后再进行锯齿形变形。但根据第 107 题实现时碰到的问题不难想到对列表进行锯齿形变形的操作会大大增加耗时([LeetCode107. 二叉树的层次遍历 II](https://www.cnblogs.com/banshaohuan/p/10830675.html))，因此我们选择在遍历过程中就将所遍历的元素直接插入到确定的位置。

分析二叉树的锯齿形遍历，其原理就在于偶数层遍历时从右往左遍历。因为我的代码中层数是从 0 开始的，所有我的判断代码为 `if level % 2 != 0 `。而在插入该所遍历元素时只需要确保每次都差入到该层列表的第一个位置即可`res[level].insert(0, root.val)`。

完整代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if root is None:
                return

            if len(res) <= level:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)

        res = []
        dfs(root, 0, res)
        return res
```
系统给出此种方法的评价为：

>Runtime: 20 ms, faster than 99.52% of Python online submissions for Binary Tree Zigzag Level Order Traversal.

>Memory Usage: 12 MB, less than 5.58% of Python online submissions for Binary Tree Zigzag Level Order Traversal.


GitHub 地址： https://github.com/protea-ban/LeetCode

![](https://img2018.cnblogs.com/blog/701977/201905/701977-20190501094902261-873549745.png)