#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (61.56%)
# Likes:    11277
# Dislikes: 1184
# Total Accepted:    1.9M
# Total Submissions: 3M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)  # 각 행(row)에서 숫자 저장
        cols = defaultdict(set)  # 각 열(column)에서 숫자 저장
        boxes = defaultdict(set)  # 각 3×3 박스에서 숫자 저장

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue  # 빈 칸은 건너뜀

                box_index = (i // 3) * 3 + (j // 3)  # 3×3 박스의 인덱스 계산

                # 중복 체크
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False  # 유효하지 않은 스도쿠

                # 숫자 추가 (중복 체크를 위해)
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True  # 유효한 스도쿠

# @lc code=end
