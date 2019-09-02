# 98. 验证二叉搜索树

### 描述

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。


### 示例

示例 1:

    输入:
        2
       / \
      1   3
    输出: true

示例 2:

    输入:
        5
       / \
      1   4
         / \
        3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
         根节点的值为 5 ，但是其右子节点值为 4 。



## 思路

### 中序遍历法

根据排序二叉树特点可知，其中序遍历的结果是递增的，因此，对二叉树进行中序遍历，判断其是否为递增序列即可知道它是不是排序二叉树。

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
```

上述代码虽然看似简单，但是在验证列表为升序排序的时候时间复杂度过大。还有一种判断其中序遍历为升序的方法，即两两相比，如果都是升序则整个排序为升序，否则不是升序。

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True

        if not self.helper(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False
        
        self.prev = root
        return self.helper(root.right)
```

### 递归法

取左子树的最大值为 min ，取右子树的最小值为 max ，根据定义，一定有 root.val > min 且 root.val < max ，对整个二叉树递归调用即可得出最终结果。
```python
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxsize - 1, sys.maxsize)

    def helper(self, root, min, max):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False

        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

```

其中， `sys.maxsize` 指系统最大值，相反， `-sys.maxsize` 指系统最小值，这种写法经常用在比较大小的入口处。

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)