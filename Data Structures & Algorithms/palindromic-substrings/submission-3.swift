class Solution {
    func countSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        
        if n < 2 {
            return n
        }

        var dp = Array(
            repeating: Array(repeating: false, count: n),
            count: n
        )

        var count = 0

        for i in 0..<n {
            dp[i][i] = true
            count += 1
        }

        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1

                if chars[i] == chars[j] && (length == 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true
                    count += 1
                }
            }
        }

        return count
    }
}
