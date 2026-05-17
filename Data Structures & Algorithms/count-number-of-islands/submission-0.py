class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            # bottom:
            dfs(row + 1, col)
            # top:
            dfs(row - 1, col)
            # left:
            dfs(row, col - 1)
            # right:
            dfs(row, col + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    # find a "1" => change everything adjacent to "0"
                    count += 1
                    dfs(row, col)

        return count
