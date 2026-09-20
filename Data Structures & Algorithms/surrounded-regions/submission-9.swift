import Collections

class Solution {
    func solve(_ board: inout [[Character]]) {
        let ROWS = board.count
        let COLS = board[0].count
        var borderOhs: Set<[Int]> = []

        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] != "O" || borderOhs.contains([r, c]) { return }

            borderOhs.insert([r, c])

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        }

        for c in 0..<COLS {
            if board[0][c] == "O" {
                dfs(0, c)
            }
            if board[ROWS - 1][c] == "O" {
                dfs(ROWS - 1, c)
            }
        }

        for r in 0..<ROWS {
            if board[r][0] == "O" {
                dfs(r, 0)
            }
            if board[r][COLS - 1] == "O" {
                dfs(r, COLS - 1)
            }
        }

        for r in 0..<ROWS {
            for c in 0..<COLS {
                board[r][c] = "X"
            }
        }

        for coord in borderOhs {
            let r = coord[0]
            let c = coord[1]
            board[r][c] = "O"
        }

    }
}
