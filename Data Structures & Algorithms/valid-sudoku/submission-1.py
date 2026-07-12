class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if (val := board[r][c]) == ".":
                    continue
                if val in rows[r] or val in columns[c] or val in boxes[r//3][c//3]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                boxes[r//3][c//3].add(val)

        return True

        