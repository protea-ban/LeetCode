### 描述
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)
### Example

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    
### 思路
1. 首先肯定要将数字和其对应的字符放到字典当中。
2. 设置一个空列表作为返回值，循环数字串中的每个数字对应的字符串，将每个字符都添加到返回列表中的每个子项的后面。