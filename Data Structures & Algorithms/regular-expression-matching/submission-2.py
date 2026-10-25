class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None] * len(p) for _ in range(len(s))]

        # 5L16
        # i indexes s; j indexes p
        def dfs(i, j) -> bool:
            # Happy (+ sad) base cases
            if j == len(p):
                return i == len(s)
            
            if i == len(s):
                aux = j
                while aux + 1 < len(p) and p[aux + 1] == '*':
                    aux += 2
                return aux == len(p)
            
            if dp[i][j] != None:
                return dp[i][j]
            
            if j + 1 < len(p) and p[j + 1] == '*':
                if s[i] == p[j] or p[j] == '.':
                    # consume s[i] or don't consume
                    dp[i][j] = dfs(i + 1, j) or dfs(i, j + 2)
                else:    
                    # don't consume
                    dp[i][j] = dfs(i, j + 2)
            else:
                # consume one in each (advance each by 1)
                dp[i][j] = (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j + 1)

            return dp[i][j]


        return dfs(0, 0)