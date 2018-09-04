# 22. 括号生成

### 描述

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。 

### 示例：

例如，给出 n = 3，生成结果为：

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

## 思路

### 思路一：暴力法

思路很简单，生成所有可能的结果，从中筛选出有效的添加到列表中，最后将列表返回即可。

此思路有两个问题要解决，第一个是如何判断有效，第二个是如何生成括号序列。

#### 判断有效
前面的第 20 题已经解决了括号匹配问题，而且是多种括号的形式，该问题只有一种括号，所以可以使用更简单的方法：**判断左右括号数量是否相等。**

#### 暴力生成所有字符串

首先判断字符串长度是否为 2*n ，如果是就判断是否有效，否则就添加 '()' 或者 ')' ,递归调用该生成函数，并 pop 出不合格的字符。

```python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(L = []):
            """
            生成序列
            :param L:
            :return:
            """
            # 序列长度为2*n，判断是否有效
            if len(L) == 2 * n:
                if valid(L):
                    ret.append("".join(L))
            else:
                # 长度不够就继续添加
                # 递归调用generate生成，无效就将最后的pop出来
                L.append('(')
                generate(L)
                L.pop()

                L.append(')')
                generate(L)
                L.pop()

        def valid(L):
            """
            校验是否有效
            :param L:
            :return:
            """
            is_valid = 0

            for i in L:
                if i == '(':
                    is_valid += 1
                else:
                    is_valid -= 1

                if is_valid < 0:
                    return False

            return is_valid == 0

        ret = []
        generate()
        return ret
```

### 思路二：递归直接生成有效序列

关键点：通过控制左右括号数量生成有效序列，只有在我们知道序列仍然保持有效时才添加 '(' 或者 ')' 。子函数可以以当前括号序列+左括号数量+右括号数量为参数，利用递归生成所有有效的括号序列。

```python
class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backTrack(L='', left=0, right=0):
            if len(L) == 2 * n:
                ret.append(L)
                return
            if left < n:
                backTrack(L+'(', left+1, right)

            if right < left:
                backTrack(L+')', left, right+1)

        ret = []
        backTrack()
        return ret
```


GitHub地址：https://github.com/protea-ban/LeetCode