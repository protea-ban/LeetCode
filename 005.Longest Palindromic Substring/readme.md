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

```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        res = ""
        for i in range(len(s)):
            # 当回文字符串长度为奇数时
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # 当回文字符串长度为偶数时
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1 : r]

if __name__ == '__main__':
    solution = Solution()
    s = "cbbd"
    res = solution.longestPalindrome(s)
    print(res)

```

GitHub地址：https://github.com/protea-ban/LeetCode