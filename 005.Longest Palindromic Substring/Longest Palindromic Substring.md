### 描述
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

### Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
### Example 2:

    Input: "cbbd"
    Output: "bb"
    
### 思路
看到官方的Solution才明白过来这是一个动态规划的问题。
如果一个字符串是回文字符串，那么在它两侧同时加上相同的字符，依然是回文字符串。<br>
即s[l]==s[r]，要考虑到回文字符串本身长度是奇数还是偶数的问题。
