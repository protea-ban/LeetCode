# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class UnorderList(object):
    """
    链表类本身不包含任何节点对象。
    相反，它只包含对链接结构中第一个节点的单个引用
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        使用引用 None 来表示链接结构的end。
        在 Python 中，None可以与任何引用进行比较。
        如果它们都指向相同的对象，则两个引用是相等的。
        :return:
        """
        return self.head is None

    def add(self, item):
        """
        添加新节点的最简单的地方就在链表的头部
        1. 更改新节点的下一个引用以引用旧链表的第一个节点
        2. 修改链表的头以引用新节点
        :param item:
        :return:
        """
        temp = ListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def searchByIndex(self, index):
        count = 0
        current = self.head

        while count < index:
            count += 1
            current = current.getNext()

        return current.getData()

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 如果要删除的项目恰好是链表中的第一个项
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def show(self):
        current = self.head
        while current is not None:
            print(current.getData(), end=' ')
            current = current.getNext()


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: UnorderList
        :type n: int
        :rtype: ListNode
        """
        # 指向头结点
        first = last = head

        # 将第一个指针后移n位，使得两个指针的间距为n-1
        for _ in range(n):
            first = first.next

        # 如果移动n位后first为空表明要删除的是第一个结点
        if not first:
            # 返回的都是头结点，此为更新头结点后返回
            return head.next

        # 两个指针同时后移
        # 当前一个指针指向尾结点时，后一个指针指向要删除的结点
        while first.next:
            first = first.next
            last = last.next

        last.next = last.next.next

        return head



if __name__ == '__main__':
    temp = [5, 4, 3, 2, 1]
    ul = UnorderList()
    so = Solution()

    for item in temp:
        ul.add(item)

    so.removeNthFromEnd(ul, 2)
    # ul.show()
