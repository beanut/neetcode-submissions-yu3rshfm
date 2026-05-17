class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    count += 1
                    grid[row][col] = "0"
                    queue = deque([(col, row)]) # deque of (col, row)
                    while queue:
                        cc, cr = queue.popleft()
                        for nc, nr in [(cc + 1, cr), (cc - 1, cr), (cc, cr + 1), (cc, cr - 1)]:
                            if nc >= 0 and nr >= 0 and nc < COLS and nr < ROWS and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nc, nr))

        return count
                                