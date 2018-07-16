class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # table = {
        #     '2': [i for i in "abc"],
        #     '3': [i for i in "def"],
        #     '4': [i for i in "ghi"],
        #     '5': [i for i in "jkl"],
        #     '6': [i for i in "mno"],
        #     '7': [i for i in "pqrs"],
        #     '8': [i for i in "tuv"],
        #     '9': [i for i in "wxyz"],
        # }

        table = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = ['']
        for digit in digits:
            temp_str = []
            for char in table[digit]:
                temp_str += [exist_str + char for exist_str in result]
            result = temp_str

        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.letterCombinations('23')
    print(result)
