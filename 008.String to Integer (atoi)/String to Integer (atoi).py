class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 用来标识数字的正负
        sign = 1

        # 表示是否找到数字
        found = False

        # 存放结果，之后有乘、加操作，所以设置初始值为0
        ret = 0

        # 去掉前后空格
        new_str = str.strip()
        for item in new_str:
            # 检测到符号
            if not found and item == "-":
                found = True
                sign = -1
            # 检测到正号
            elif not found and item == "+":
                found = True
            # 检测到数字
            elif item.isdigit():
                found = True
                ret = ret * 10 + int(item)

                # 超出范围返回规定的数字
                if ret > 2147483647 and sign == 1:
                    return 2147483647
                elif ret > 2147483648 and sign == -1:
                    return -2147483648
            else:
                break

        return sign * ret


if __name__ == '__main__':
    so = Solution()
    # str = "   -42"
    str = "4193 with words"
    # str = "words and 987"
    # str = "-91283472332"
    ret = so.myAtoi(str)
    print(ret)
