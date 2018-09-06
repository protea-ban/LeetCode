# 3. 无重复字符的最长子串

### 问题描述
> Given a string, find the length of the longest substring without repeating characters.
### Example
> Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
### 思路
问题即是求字符串中的最长子序列。

1. low方法：循环解决

    双重循环，判断是否字符在子序列中。
2. NB方法：放入字典

    字典中存放字符及其出现的位置索引，不断更新。
    
```python
class Solution:
    def lengthOfLongestSubstring0(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        if (len(s) == 1 or len(s) == 0):
            max_length = len(s)
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    if j - i > max_length:
                        max_length = j - i
                    break
                elif j == len(s) - 1:
                    if max_length < j - i + 1:
                        max_length = j -i + 1
        return max_length

    def lengthOfLongestSubstring(self, s):
        indexDict = {}
        maxLength = currMax = 0

        for i in range(len(s)):
            if s[i] in indexDict and i - indexDict[s[i]] - 1 <= currMax:
                if maxLength < currMax:
                    maxLength = currMax
                currMax = i - indexDict[s[i]] - 1
            currMax = currMax + 1
            indexDict[s[i]] = i

        return maxLength if currMax < maxLength else currMax


if __name__ == '__main__':
    solution = Solution()
    max_length = solution.lengthOfLongestSubstring('abcabcbb')
    print(max_length)
```


GitHub地址：https://github.com/protea-ban/LeetCode