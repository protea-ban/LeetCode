# 23. 合并K个排序链表

### 描述

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

### 示例

    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
 
## 思路

### 思路一

这道题是第 21 道题的升级版，所以可以借助第 21 题的算法。

方法是重复将列表中的前两个合并排序成一个，直到最后变成一个有序的链表。

而参考答案中提出了一个类似于这种却比这种优越的方法：不是将列表总的前两个链表合并排序，而是将列表中的所有链表两个两个合并，直到剩下最后一个链表，下图可以很好的展示此方法。

![](http://pdg1wvjcw.bkt.clouddn.com/kkk.png)

```python
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
```

时间复杂度分析：

O(N log k), 其中 N 为所有链表的节点数目，K 为链表的数目。

### 思路二

将所有链表中的节点都放在同一个列表中，对该列表进行排序后，将列表变成一个链表。

```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
```

时间复杂度分析：

O(N log N) 其中 N 为所有节点的总数。

GitHub地址：https://github.com/protea-ban/LeetCode