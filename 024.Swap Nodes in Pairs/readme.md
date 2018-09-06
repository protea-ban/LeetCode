# 24. 两两交换链表中的节点

### 描述

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

### 示例

    给定 1->2->3->4, 你应该返回 2->1->4->3.
   
说明:

- 你的算法只能使用常数的额外空间。
- **你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

## 思路

链表的交换其实就是指针的交换，要比列表中进行交换要方便一些。

实现过程：

![](http://pdg1wvjcw.bkt.clouddn.com/image/blog/leetcode24_1.jpg)

![](http://pdg1wvjcw.bkt.clouddn.com/image/blog/leetcode24_2.jpg)

![](http://pdg1wvjcw.bkt.clouddn.com/image/blog/leetcode24_3.jpg)

![](http://pdg1wvjcw.bkt.clouddn.com/image/blog/leetcode24_4.jpg)

后移后重复上述过程，直到循环结束。 （图片来源于网络）

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = cur = ListNode(0)
        cur.next = head

        # 终止条件：cur指向的节点并不交换，交换的是cur指针后的两个节点
        while cur.next and cur.next.next:
            cur.next.next.next, cur.next.next, cur.next, cur = cur.next, cur.next.next.next, cur.next.next, cur.next

        return ret.next

```

GitHub地址：https://github.com/protea-ban/LeetCode