from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def figure_box(i, j):
            row = int(i)
            col = int(j)
            if 0 <= row <= 2 and 0 <= col <= 2:
                return 0
            elif 0 <= row <= 2 and 3 <= col <= 5:
                return 1
            elif 0 <= row <= 2 and 6 <= col <= 8:
                return 2
            elif 3 <= row <= 5 and 0 <= col <= 2:
                return 3
            elif 3 <= row <= 5 and 3 <= col <= 5:
                return 4
            elif 3 <= row <= 5 and 6 <= col <= 8:
                return 5
            elif 6 <= row <= 8 and 0 <= col <= 2:
                return 6
            elif 6 <= row <= 8 and 3 <= col <= 5:
                return 7
            elif 6 <= row <= 8 and 6 <= col <= 8:
                return 8

        hash_row = defaultdict(set)
        hash_col = defaultdict(set)
        hash_box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                spot = figure_box(i, j)
                if v in hash_row[i] or v in hash_col[j] or v in hash_box[spot]:
                    return False
                if v != ".":
                    hash_row[i].add(v)
                    hash_col[j].add(v)
                    hash_box[spot].add(v)
        
        return True
