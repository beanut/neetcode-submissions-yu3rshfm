import Collections

class Solution {
    struct Point: Hashable {
        let r: Int
        let c: Int
    }

    func islandsAndTreasure(_ grid: inout [[Int]]) {
        guard !grid.isEmpty, !grid[0].isEmpty else { return }

        let rows = grid.count
        let cols = grid[0].count

        var visited: Set<Point> = []
        var queue: Deque<(Int, Int)> = []

        func addRoom(_ r: Int, _ c: Int) {
            guard r >= 0, r < rows,
                  c >= 0, c < cols,
                  grid[r][c] != -1,
                  !visited.contains(Point(r: r, c: c))
            else { return }

            visited.insert(Point(r: r, c: c))
            queue.append((r, c))
        }

        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] == 0 {
                    queue.append((r, c))
                    visited.insert(Point(r: r, c: c))
                }
            }
        }

        var distance = 0

        while !queue.isEmpty {
            let levelSize = queue.count

            for _ in 0..<levelSize {
                let (r, c) = queue.popFirst()!
                grid[r][c] = distance

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            }

            distance += 1
        }
    }
}