from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        completed = False
        while not completed:
            # update suggestion
            for y in range(9):
                for x in range(9):
                    if board[y][x] != '.':
                        continue

                    # in block
                    # block = y // 3 * 3 + x // 3
                    # for by in range(y // 3 * 3, y // 3 * 3 + 3):
                    #     for bx in range(x // 3 * 3, x // 3 * 3 + 3):
                    #         print(bx, by)

            # # set suggestions by 3x3 blocks
            # for block in range(9):
            #     for y in range(3):
            #         yy = y + (block // 3) * 3
            #         for x in range(3):
            #             xx = x + (block % 3) * 3
            #             if board[yy][xx] != '.':
            #                 continue
            #             board[yy][xx] = []

            completed = True
