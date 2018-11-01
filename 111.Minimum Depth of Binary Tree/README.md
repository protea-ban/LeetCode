# 111.二叉树的最小深度

### 描述

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

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
返回它的最小深度  2.

## 思路

乍一看跟上一题求最大深度一样，将 max 函数换成 min 函数试试。

提交后果然出错了，给了一个报错的例子 [1, 2] ，就是 root 只有一个右孩子或者左孩子的特殊情况。这种情况下，在没有孩子的那个字树中自认返回的是 0 ，故而最终结果为 0 。

应对这种情况，进行一下判断即可。

```python
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1
```



GitHub地址：https://github.com/protea-ban/LeetCode