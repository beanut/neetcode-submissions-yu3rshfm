class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True)

        wordDict = {w : i for i, w in enumerate(words)}

        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            w = words[i]
            res = 1
            for j in range(len(w)):
                x = w[:j] + w[j + 1:]
                if x not in wordDict:
                    continue
                res = max(res, 1 + dfs(wordDict[x]))
            
            dp[i] = res
            return dp[i]

        return max(
            dfs(i)
            for i in range(len(words))
        )
