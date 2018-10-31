# 104.二叉树的最大深度

### 描述

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

### 示例

给定二叉树 [3,9,20,null,null,15,7]，
```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度 3 。

## 思路

该题要求返回一个二叉树的深度。

可以使用 map 函数让左子树和右子树一起调用求深度的函数，返回最大值即可。

```python
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
```


GitHub地址：https://github.com/protea-ban/LeetCode