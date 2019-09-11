class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return 
        self.solve(board)

    def solve(self, board):
        choice = [str(i) for i in range(1, 10)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in choice:
                        if self.is_Valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        
        return True

    def is_Valid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != "." and board[i][col] == c:
                return False
            if board[row][i] != "." and board[row][i] == c:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] != "." and board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
        return True
            
            