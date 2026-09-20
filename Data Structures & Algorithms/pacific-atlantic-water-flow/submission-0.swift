import Collections

class Solution {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        let ROWS = heights.count
        let COLS = heights[0].count

        let dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        var pac: Set<[Int]> = [] // cells that can reach the pacific
        var atl: Set<[Int]> = [] // cells that can reach the atl

        func dfs(_ r: Int, _ c: Int, _ visited: inout Set<[Int]>, _ prevHeight: Int) {
            if r < 0 || c < 0 || r >= ROWS || c >= COLS || visited.contains([r, c]) || heights[r][c] < prevHeight { return }

            visited.insert([r, c])

            for d in dirs {
                let nr = r + d[0]
                let nc = c + d[1]

                dfs(nr, nc, &visited, heights[r][c])
            }
        }

        for c in 0..<COLS {
            dfs(0, c, &pac, heights[0][c])
            dfs(ROWS - 1, c, &atl, heights[ROWS - 1][c])
        }

        for r in 0..<ROWS {
            dfs(r, 0, &pac, heights[r][0])
            dfs(r, COLS - 1, &atl, heights[r][COLS - 1])
        }

        let ret: [[Int]] = Array(pac.intersection(atl))

        return ret
    }
}
