class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = defaultdict(set)
        vertical   = defaultdict(set)
        squares    = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in horizontal[r] or
                    board[r][c] in vertical[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                horizontal[r].add(board[r][c])
                vertical[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True        
      
         