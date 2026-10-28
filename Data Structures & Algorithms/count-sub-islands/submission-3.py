class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])

        count = 0
        q = deque()


        def bfs() -> bool:
            isSubisland = True
            while q:
                cur = q.popleft()
                if grid1[cur[0]][cur[1]] != 1:
                    isSubisland = False
                for (i, j) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr = cur[0] + i
                    nc = cur[1] + j
                    
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid2[nr][nc] == 1:
                        q.append([nr, nc])
                        grid2[nr][nc] = 0
            
            return isSubisland

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c]:
                    q.append([r, c])
                    grid2[r][c] = 0
                    count += 1 if bfs() else 0

        return count