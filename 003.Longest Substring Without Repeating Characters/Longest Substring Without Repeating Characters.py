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