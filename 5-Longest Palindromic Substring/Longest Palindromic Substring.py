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
