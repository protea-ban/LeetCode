# 108. 将有序数组转换为二叉搜索树

### 问题描述

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

### 示例

	给定的有序数组： [-10, -3, 0, 5, 9],

	一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

		  0
		 / \
	   -3   9
	   /   /
	 -10  5


### 思路

递归

- nums为空，return None
- nums非空，nums[n/2]为中间元素，根结点，nums[:mid]为左子树， nums[mid+1:]为右子树

```python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```

GitHub地址：https://github.com/protea-ban/LeetCode