# 109. 有序链表转换二叉搜索树

### 问题描述

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

### 示例

	给定的有序链表： [-10, -3, 0, 5, 9],

	一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

		  0
		 / \
	   -3   9
	   /   /
	 -10  5


### 思路

与 108 很类似，无非是将有序数组变成了有序链表，最省事的方法就是将有序链表变成有序数组，然后继续用 108 的思路进行解决。

**递归**

- nums为空，return None
- nums非空，nums[n/2]为中间元素，根结点，nums[:mid]为左子树， nums[mid+1:]为右子树

```python
class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(nums):
            if not nums:
                return None
            if nums:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = sortedArrayToBST(nums[:mid])
                root.right = sortedArrayToBST(nums[mid+1:])

        if not head:
            return None
        else:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next

        return sortedArrayToBST(lst)

```

GitHub地址：https://github.com/protea-ban/LeetCode