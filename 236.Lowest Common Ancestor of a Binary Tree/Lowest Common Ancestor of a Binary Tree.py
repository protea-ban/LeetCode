# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 15:58
# @Author  : banshaohuan
# @Site    : 
# @File    : Lowest Common Ancestor of a Binary Tree.py
# @Software: PyCharm
class Solution1(object):
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
