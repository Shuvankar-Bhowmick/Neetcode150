'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each of rows, columns, and squares will have a hashset to their name
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # key->(r // 3, c //3): value->set

        for r in range(9):
            for c in range(9):
                # check for the rows, cols, entire 3 x 3 grid
                if board[r][c] != ".":
                    if (board[r][c] in rows[r] or 
                        board[r][c] in cols[c] or 
                        board[r][c] in square[(r // 3, c // 3)]):
                        return False
                    else:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        square[(r // 3, c // 3)].add(board[r][c])
        return True
                
                    