# 242. 有效的字母异位词

### 描述

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

### 示例

示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true

示例 2:

    输入: s = "rat", t = "car"
    输出: false


## 思路


### 排序法

对两个字符串进行排序，若满足题目要求则其排序后定相等。

```python
# 排序法 O(NlogN)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
```

即使使用最快的快排方法，时间复杂度也有O(NlogN)

### 哈希计数法

根据定义，每个字符串的中的每个字符的数量是相同的，所以，对每个字符串进行哈希计数，若两个哈希表相同，则返回 True ，Python 中使用字典来实现哈希表。

```python
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}

        for item_s in s:
            if item_s not in s_dict:
                s_dict[item_s] = 1
            else:
                s_dict[item_s] += 1

        for item_t in t:
            if item_t not in t_dict:
                t_dict[item_t] = 1
            else:
                t_dict[item_t] += 1

        return s_dict == t_dict
```

上述代码中包含了一个非常典型的用法：判断字典中是否有该键，没有时将键加进去赋值，有时做另外处理。即：

```python
if item_s not in s_dict:
    s_dict[item_s] = 1
else:
    s_dict[item_s] += 1
```

可以用一种更为简单的写法代替：

```python
s_dict[item_s] = s_dict.get(item_s, 0) + 1
```

GitHub地址：https://github.com/protea-ban/LeetCode

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)