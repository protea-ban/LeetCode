### 描述
Given a linked list, remove the n-th node from the end of list and return its head.

### Example

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
    
### 思路
1. 考虑使用两个指针
2. 首先让两个指针指向头结点，第一个指针向后移动 n 位，使得两个指针间隔为 n-1 
3. 两个指针同时往后移动，当第一个指针指向尾结点时，后一个指针则指向从后向前数的第 n 个结点
4. 注意特殊情况：要删除的是第一个结点