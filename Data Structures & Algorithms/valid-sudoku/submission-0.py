class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_table = defaultdict(list)
        rows_table = defaultdict(list)
        square_table = defaultdict(list)

        for y in range(9):
            for x in range(9):
                sq_index = (y // 3) * 3 + (x // 3)
                # print(f"row is: {y} - col is: {x} - sq_index is: {sq_index}")
                converted = 0
                if board[y][x] == '.':
                    pass
                else:
                    converted = int(board[y][x])
                if converted != 0 and (converted in cols_table[x] 
                    or converted in rows_table[y]
                    or converted in square_table[sq_index]):
                    return False
                rows_table[y].append(converted)
                cols_table[x].append(converted)
                square_table[sq_index].append(converted)
        
        return True
