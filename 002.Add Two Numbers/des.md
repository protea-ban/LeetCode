### 问题描述
> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example

> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

### 思路
==问题：== 两个链表分别倒叙存储两个数的每一位数值，即342存储为(2 -> 4 -> 3)，返回两数之和的链表形式。

1. 两个链表从表头开始相加，注意进位。
2. 考虑到两个链表长度不同的情况。
