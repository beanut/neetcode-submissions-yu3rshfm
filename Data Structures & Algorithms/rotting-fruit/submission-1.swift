import Collections

class Solution {
    struct Pt: Hashable {
        let r: Int
        let c: Int

        init(_ r: Int, _ c: Int) {
            self.r = r
            self.c = c
        }
    }

    func orangesRotting(_ grid: [[Int]]) -> Int {
        let ROWS = grid.count
        let COLS = grid[0].count

        var seen: Set<Pt> = []

        var q: Deque<Pt> = []

        var oranges = 0

        func process(_ r: Int, _ c: Int) {
            if r < 0 || r >= ROWS || c < 0 || c >= COLS || seen.contains(Pt(r, c)) || grid[r][c] != 1 { return }

            seen.insert(Pt(r, c))
            q.append(Pt(r, c))
            oranges -= 1
        }

        for r in 0..<ROWS {
            for c in 0..<COLS {
                if grid[r][c] == 2 {
                    seen.insert(Pt(r, c))
                    q.append(Pt(r, c))
                }
                if grid[r][c] == 1 {
                    oranges += 1
                }
            }
        }

        var mins = 0
        while !q.isEmpty && oranges > 0 {
            for _ in 0..<q.count {
                let pt = q.popFirst()!
                let r = pt.r
                let c = pt.c

                process(r - 1, c)
                process(r + 1, c)
                process(r, c - 1)
                process(r, c + 1)
            }
            mins += 1
        }

        return oranges == 0 ? mins : -1 
    }
}
