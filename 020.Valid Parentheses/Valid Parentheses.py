class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Solution1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # from pythonds.basic.stack import Stack
        stack = Stack()
        balanced = True
        index = 0

        while index < len(s) and balanced:
            index_s = s[index]
            if index_s in "([{":
                stack.push(index_s)
            else:
                # 如果当前字符不是开括号且栈为空，则一定不匹配
                if stack.isEmpty():
                    balanced = False
                else:
                    top = stack.pop()
                    if not self.matchs(top, index_s):
                        balanced = False

            index += 1

        if balanced and stack.isEmpty():
            return True
        else:
            return False

    def matchs(self, start, end):
        """
        通过定义字符串，根据字符串的下标是否相同
        来检查括号是否匹配
        :param start: 开括号
        :param end: 闭括号
        :return:
        """
        starts = "([{"
        ends = ")]}"

        return starts.index(start) == ends.index(end)


class Solution2:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack or d[stack.pop()] != i:
                    return False

        else:
            if stack:
                return False

        return True


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_num = len(s)

        # 默认空字符串为TRUE
        if len_num == 0:
            return True

        # 字符数为奇数，不可能匹配
        if len_num % 2 != 0:
            return False

        while '()' in s or '[]' in s or '{}' in s:
            s.replace("()", "").replace("[]", "").replace("{}", "")

        return s == ''


if __name__ == '__main__':
    so = Solution()
    print(so.isValid("()"))
