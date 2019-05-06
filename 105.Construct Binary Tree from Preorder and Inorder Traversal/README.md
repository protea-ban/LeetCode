# 105. 从前序与中序遍历序列构造二叉树


### 描述

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

### 示例

例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

## 思路

一颗二叉树，对于前序遍历来说，其第一个元素一定是这棵树的根节点。在中序遍历中找到这个元素所在的位置，那么它的左半部分就是其左子树，右半部分就是其右子树。

重复上述过程， 通过前序遍历找到根节点， 然后在中序遍历数据中根据根节点拆分成两个部分， 同时将对应的前序遍历的数据也拆分成两个部分， 重复递归， 就可以得到整个二叉树了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root
```

GitHub 地址： https://github.com/protea-ban/LeetCode

![](https://img2018.cnblogs.com/blog/701977/201905/701977-20190501094902261-873549745.png)