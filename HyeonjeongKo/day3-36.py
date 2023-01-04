class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row중복체크 ; 숫자만남기고 중복 체크(set이용)
        for i in range(9):
            row = list(filter(lambda x: x.isalnum(),board[i]))
            if len(row) != len(set(row)):
                return False

        # col중복체크 ; 전치후 숫자만남기고 중복 체크(set이용)
        board_t = list(zip(*board))

        for i in range(9):
            col = list(filter(lambda x: x.isalnum(),board_t[i]))
            if len(col) != len(set(col)):
                return False

        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in boxes[(r//3,c//3)]):
                    return False
                boxes[(r//3,c//3)].add(board[r][c])

        return True
