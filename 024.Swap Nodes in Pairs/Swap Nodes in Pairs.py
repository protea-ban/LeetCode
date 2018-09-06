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
