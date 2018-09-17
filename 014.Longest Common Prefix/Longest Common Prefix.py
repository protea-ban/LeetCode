class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 特殊情况：没有字符串/有一个字符串
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        len_strs = len(strs)
        # 最大长度为所有字符串中长度最短的那个
        max_len_prefix = min([len(str) for str in strs])

        for idx_pre in range(0, max_len_prefix):
            for idx_strs in range(1, len_strs):
                if strs[0][idx_pre] != strs[idx_strs][idx_pre]:
                    return strs[0][:idx_pre]

        # 如果在for中没返回，则最长的前缀长度就为max_len_prefix
        return strs[0][:max_len_prefix]


if __name__ == '__main__':
    so = Solution()
    # strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    # strs = ["", ""]
    print(so.longestCommonPrefix(strs))
