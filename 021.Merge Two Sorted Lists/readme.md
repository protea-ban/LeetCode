# 21. 合并两个有序链表

### 描述

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

### 示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

## 思路

### 1. 普通思路

借助原本链表有序，从头开始比较原有两个链表，将值较小链表（记为链表 L ）的节点插入新链表中，同时移动 L 的指针后移，重复这个过程，直到有一个原链表全部插入到新链表中。

因为原有两个链表有序，剩下的那个链表就直接接在新链表尾部即可。

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = l3 = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            # 值较小的接在目标链接后并将新链表指针后移
            l3 = l3.next

        if l1:
            l3.next = l1

        if l2:
            l3.next = l2

        return ret.next
```
### 2. 递归

可以采用递归的思路，链表指针往后移动依旧可以看做是一个链表，所以可以反复调用这个方法，只需将参数改成该链表除去当前节点的链表和另一个没有改动的链表即可。

此方法比上面那种效率要高。

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```