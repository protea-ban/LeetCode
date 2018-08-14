# 20. 有效的括号

### 描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

### Example

示例 1:

    输入: "()"
    输出: true
示例 2:

    输入: "()[]{}"
    输出: true
示例 3:

    输入: "(]"
    输出: false
示例 4:

    输入: "([)]"
    输出: false
示例 5:

    输入: "{[]}"
    输出: true
    
### 思路
#### 1. 使用栈
提到括号匹配立马能想到的肯定就是栈了。

对要进行匹配的字符串依次入栈，有下面几种情况：
1. 当前字符为开括号，入栈
2. 当前字符为闭括号：
    1. 若栈为空，能得出不匹配的结论
    2. 栈不为空，出栈，出栈字符与当前字符串是否正好匹配，匹配就进入下一字符，否则不匹配
    
 我实现的代码比较繁琐，想导入 python 自带的库来实现栈，但 LeetCode 不支持，只好自己用代码实现。效果不怎么好，beat 掉 60% 。
 
 ```python
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

class Solution:
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
```

再来看别人同样用栈。方法是直接使用 list 的 pop 和 append 方法实现栈，beat 掉了 99% 之多，我觉得可能是由于他有直接 return 而我是最后一起 return 的。

```python
class Solution:
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
```

### 2. 巧用 replace 函数
这个方法我只能说比较贼了。

利用 replace 函数不断将已经成对的括号组替换成空字符串，若最后字符串为空则是匹配的。这个能 beat 掉多少我也没试。

```python
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
```
GitHub地址：https://github.com/protea-ban/LeetCode