#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: Add Two Numbers.py 
@time: 2018/06/10
@contact: banshaohuan@163.com
@software: PyCharm  
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #=> p和dummy都是指向最终返回的链表的表头，p用于操作，dummy用于最后返回
        p = dummy = ListNode(-1)
        #=> carry为进位标志，初始值为0
        carry = 0
        #=> 对于两个链表共有节点的处理
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            carry = int(p.next.val / 10)
            p.next.val %= 10
            p = p.next
            l1 = l1.next
            l2 = l2.next

        #=> "或"操作得到较长那个链表的剩余部分
        res = l1 or l2
        #=> 剩余部分的处理
        while res:
            p.next = ListNode(res.val + carry)
            carry = int(p.next.val / 10)
            p.next.val %= 10
            p = p.next
            res = res.next
        #=> 考虑到最高位也有可能进位
        if carry:
            p.next = ListNode(1)

        return dummy.next