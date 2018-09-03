# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
