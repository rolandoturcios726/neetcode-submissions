class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _  in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                if val in columns[c]:
                    return False
                if val in boxes[r//3][c//3]:
                    return False
                columns[c].add(val)
                rows[r].add(val)
                boxes[r//3][c//3].add(val)

        return True
                    
                
                