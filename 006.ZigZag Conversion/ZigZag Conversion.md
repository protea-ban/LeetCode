### 描述
> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
> And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:<br>
`string convert(string s, int numRows);`

### Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
### Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    
### 思路
如果稍微考虑的数学一点，那么s中的第i个字符（下标从第0个开始），如果按照zigzag书写方式会出现在的行数为（行数为0到numRows-1行）：
 
- i % (2 * numRows - 2), if i % (2 * numRows - 2) < numRows 
- 2 * numRows - 2 - (i % (2 * numRows - 2)), if i % (2 * numRows - 2) >= numRows 

有了这个结果，对于任意一个位置的字符我们都知道它应该在第几行。