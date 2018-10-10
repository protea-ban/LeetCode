class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        rowNumber = 0
        colNumber = len(matrix[0]) - 1

        while ((rowNumber < len(matrix)) and (colNumber >= 0)):
            if target < matrix[rowNumber][colNumber]:
                colNumber -= 1
            elif target > matrix[rowNumber][colNumber]:
                rowNumber += 1
            else:
                return True

        return False


if __name__ == '__main__':
    so = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    print(so.searchMatrix(matrix, target))
