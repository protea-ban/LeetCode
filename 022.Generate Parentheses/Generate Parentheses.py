class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(L = []):
            """
            生成序列
            :param L:
            :return:
            """
            # 序列长度为2*n，判断是否有效
            if len(L) == 2 * n:
                if valid(L):
                    ret.append("".join(L))
            else:
                # 长度不够就继续添加
                # 递归调用generate生成，无效就将最后的pop出来
                L.append('(')
                generate(L)
                L.pop()

                L.append(')')
                generate(L)
                L.pop()

        def valid(L):
            """
            校验是否有效
            :param L:
            :return:
            """
            is_valid = 0

            for i in L:
                if i == '(':
                    is_valid += 1
                else:
                    is_valid -= 1

                if is_valid < 0:
                    return False

            return is_valid == 0

        ret = []
        generate()
        return ret


class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backTrack(L='', left=0, right=0):
            if len(L) == 2 * n:
                ret.append(L)
                return
            if left < n:
                backTrack(L+'(', left+1, right)

            if right < left:
                backTrack(L+')', left, right+1)

        ret = []
        backTrack()
        return ret


if __name__ == '__main__':
    so = Solution()
    ret = so.generateParenthesis(3)
    print(ret)
