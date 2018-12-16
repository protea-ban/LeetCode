# 61. 旋转链表

### 题目描述

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

### 示例

示例 1:

    输入: 1->2->3->4->5->NULL, k = 2
    输出: 4->5->1->2->3->NULL
    解释:
    向右旋转 1 步: 5->1->2->3->4->NULL
    向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

    输入: 0->1->2->NULL, k = 4
    输出: 2->0->1->NULL
    解释:
    向右旋转 1 步: 2->0->1->NULL
    向右旋转 2 步: 1->2->0->NULL
    向右旋转 3 步: 0->1->2->NULL
    向右旋转 4 步: 2->0->1->NULL

## 思路

题目说是链表的每个节点移动，因为是旋转链表，所有实际上是头指针和尾指针的移动。

由示例 2 可以看出，k 的值可能比链表的 size 更大，所以取余得最终移动次数。

首先还是得判断为 None 的情况。

应该从尾指针开始移动，然后进行头指针的移动。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head

        # 当前指针
        cur = head
        size = 1
        # 循环链表，获取链表长度
        while cur.next:
            size += 1
            cur = cur.next

        # 尾指针
        tail = cur

        # 旋转链表，获取真正要移动的次数
        k = k % size
        
        p = self.findKth(head, k)
        
        tail.next = head
        head = p.next
        p.next = None
        
        return head

    def findKth(self, head, k):
        # dummy为尾指针
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy

        # 代表尾指针的q后移k位
        for i in range(k):
            q = q.next

        # p是头指针的前一个节点
        while q.next:
            p = p.next
            q = q.next

        return p

```

GitHub地址：https://github.com/protea-ban/LeetCode