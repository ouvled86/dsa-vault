class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        ret = 0
        max_x = len(grid[0])
        max_y = len(grid)
        visited = set()

        def bfs(grid, y, x, visited):
            q = collections.deque()
            q.append((y, x))
            bounds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for i, j in bounds:
                r, c = y + i, x + j
                if (
                    r >= 0 and r < max_y 
                    and c >= 0 and c < max_x
                    and grid[r][c] == "1"
                    and (r, c) not in visited
                ):
                    visited.add((r, c))
                    bfs(grid, r, c, visited)

                    
        for y in range(max_y):
            for x in range(max_x):
                if (
                    grid[y][x] == "1"
                    and (y, x) not in visited
                ):
                    visited.add((y, x))
                    bfs(grid, y, x, visited)
                    ret += 1

        
        return ret

