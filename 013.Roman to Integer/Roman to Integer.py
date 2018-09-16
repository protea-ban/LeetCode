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


if __name__ == '__main__':
    so = Solution()
    s = "III"
    # s = "IX"
    # s = "MCMXCIV"
    print(so.romanToInt(s))
