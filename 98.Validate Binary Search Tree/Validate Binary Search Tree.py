# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 12:21
# @Author  : banshaohuan
# @Site    : 
# @File    : Validate Binary Search Tree.py
# @Software: PyCharm
class Solution1(object):
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


class Solution2(object):
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
