# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS方法
class Solution1(object):
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


# BFS方法
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque()
        queue.append(root)

        # visited = set(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)

        return result


if __name__ == '__main__':
    pass
