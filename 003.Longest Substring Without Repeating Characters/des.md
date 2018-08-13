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