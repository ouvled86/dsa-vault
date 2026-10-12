class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curr_time = 0
        max_x = len(grid[0])
        max_y = len(grid)
        fresh = 0
        q = collections.deque()

        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 1:
                    fresh += 1
                if grid[y][x] == 2:
                    q.append([y, x])

        bounds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for k in range(len(q)):
                r, c = q.popleft()
                for i, j in bounds:
                    row, col = r + i, c + j
                    if (row < 0 or row >= max_y
                        or col < 0 or col >= max_x
                        or grid[row][col] != 1):
                        continue
                    fresh -= 1
                    grid[row][col] = 2
                    q.append([row, col])
            curr_time += 1
            
        print(fresh)
        print(curr_time)
        return -1 if fresh > 0 else curr_time

                    