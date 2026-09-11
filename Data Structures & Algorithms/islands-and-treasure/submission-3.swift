import Collections

class Solution {

    struct Point: Hashable {
        let r: Int
        let c: Int
    }
    func islandsAndTreasure(_ grid: inout [[Int]]) {
        let ROWS = grid.count
        let COLS = grid[0].count

        var visit: Set<Point> = []

        var q: Deque<(Int, Int)> = []

        func addRoom(_ r: Int, _ c: Int) {
            if r < 0 || r >= ROWS || c < 0 || c >= COLS || visit.contains(Point(r: r, c: c)) || grid[r][c] == -1 { return }

            visit.insert(Point(r: r, c: c))
            q.append((r, c))
        }

        for r in 0..<ROWS {
            for c in 0..<COLS {
                if grid[r][c] == 0 {
                    q.append((r, c))
                    visit.insert(Point(r: r, c: c))
                }
            }
        }

        var dist = 0
        while !q.isEmpty {
            for i in 0..<q.count {
                let (r, c) = q.popFirst()!

                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            }

            dist += 1
        }

    }
}
