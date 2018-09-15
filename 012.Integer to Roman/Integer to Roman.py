class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        values = {"M": 1000, "D": 500, "C": 100, "L": 50,\
        "X": 10, "V": 5, "I": 1}
        literals = ["M", "D", "C", "L", "X", "V", "I"]

        # 依次除以1000,100,10
        for idx in [0, 2, 4]:
            # k表示整除得到的商
            k = num // values[literals[idx]]
            re = (num % values[literals[idx]])\
            // values[literals[idx + 2]]

            # 加上相应的罗马字符
            ret += k * literals[idx]

            # 分情况处理
            if re >= 9:
                ret += literals[idx + 2] + literals[idx]
            elif re >= 5:
                ret += literals[idx + 1] + (re - 5) * literals[idx + 2]
            elif re == 4:
                ret += literals[idx + 2] + literals[idx + 1]
            else:
                ret += re * literals[idx + 2]

            # 进入下一轮循环
            num %= values[literals[idx + 2]]

        return ret


if __name__ == '__main__':
    so = Solution()
    num = 10
    ret = so.intToRoman(num)
    print(ret)
