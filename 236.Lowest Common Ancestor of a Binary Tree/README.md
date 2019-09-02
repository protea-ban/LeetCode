# 236. 二叉树的最近公共祖先

### 题目描述

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

### 示例

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

![](https://raw.githubusercontent.com/protea-ban/images/master/20190902160557.png)

示例 1:

    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出: 3
    解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:

    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出: 5
    解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉树中。

### 思路

#### 路径比较法

首先，分别找到从根结点到这两个结点的路径；然后，遍历这两条路径，只要是相等的结点就是他们的公共祖先，找到最后一个相等的结点就是他们的最近公共祖先。

在这里我们用模拟栈来进行路径寻找。

```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s1 = []
        s2 = []

        self.getPathFromRoot(root, p, s1)
        self.getPathFromRoot(root, q, s2)
        commonParent = None

        while len(s1) != 0 and len(s2) != 0 and s1[len(s1)-1] == s2[len(s2)-1]:
            commonParent = s1[len(s1)-1]
            s1.pop()
            s2.pop()

        return commonParent


    def getPathFromRoot(self, root, node, s):
        if root is None:
            return False

        if root == node:
            s.append(root)
            return True

        if self.getPathFromRoot(root.left, node, s) or self.getPathFromRoot(root.right, node, s):
            s.append(root)
            return True

        return False
```

#### 递归法

首先，如果 root 是 p 或 q 其中的一个，那么 root 就是最近公共祖先。否则，在 root 的左子树中查找 p 和 q ，如果不在，则公共祖先在 root 的右子树中，反之亦然。

```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)