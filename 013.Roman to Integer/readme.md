# 13. 罗马数字转整数

### 描述

罗马数字包含以下七种字符：I， V， X， L，C，D 和 M。

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

### 示例

示例 1:

    输入: "III"
    输出: 3

示例 2:

    输入: "IV"
    输出: 4

示例 3:

    输入: "IX"
    输出: 9

示例 4:

    输入: "LVIII"
    输出: 58
    解释: C = 100, L = 50, XXX = 30, III = 3.

示例 5:

    输入: "MCMXCIV"
    输出: 1994
    解释: M = 1000, CM = 900, XC = 90, IV = 4.

## 思路

### 思路一

可以知道的情况是需要处理两种情况：
1. 一个罗马字符为数值
2. 两个罗马字符为数值

所以，可以暴力罗列出所有的情况，作为一个字典，遍历字符串，在字典中进行匹配，需要注意两个字符进行匹配的情形。

```python
class Solution0:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"M": 1000, "D": 500, "C": 100, "L": 50,\
                  "X": 10, "V": 5, "I": 1, 'IV': 4, "IX": 9, "XL": 40, "XC": 90, "CD":400, "CM": 900}

        i, ret = 0, 0

        while i < len(s):
            # 同时取出两个罗马字符，看在字典中是否存在
            # 如果存在，加入数值当中并且i向后移动两位
            if i < len(s) - 1 and values.get(s[i: i+2]) is not None:
                i, ret = i+2, ret+values.get(s[i: i+2])
            # 不存在，将第一个数值加入并后移一位
            else:
                i, ret = i+1, ret + values.get(s[i])

        return ret
```

### 思路二

另一种方法可以根据罗马数字的运算规律找方法。

即，罗马数字中，高位在左，高位字符代表的数值小于前一位字符代表数值为相减，否则为相加。

```python
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, \
                  "X": 10, "V": 5, "I": 1}
        # 需要用一个变量记录前面一个字符代表的数字
        prev_value = total_value = 0

        # 从右往左处理
        for i in range(len(s)-1, -1, -1):
            int_val = values[s[i]]

            # 如果当前值小于前一位，减
            if int_val < prev_value:
                total_value -= int_val
            # 当前值大于前一位，加
            else:
                total_value += int_val

            # 更新当前值
            prev_value = int_val

        return total_value

```

GitHub地址：https://github.com/protea-ban/LeetCode