class Solution {
    func longestPalindrome(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count

        if n < 2 {
            return s
        }

        var dp = Array(
            repeating: Array(repeating: false, count: n),
            count: n
        )

        // prefill 1-char substrings:
        for i in 0..<n {
            dp[i][i] = true
        }

        var l = 0
        var r = 0

        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1

                if chars[i] == chars[j] && (length == 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true

                    if length > r - l + 1 {
                        l = i
                        r = j
                    }
                }
            }
        }

        return String(chars[l...r])
    }
}
