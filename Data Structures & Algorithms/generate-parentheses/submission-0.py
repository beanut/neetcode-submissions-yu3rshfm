class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(o: int, c: int, cur: str):
            if o == n and c == n:
                res.append(cur)
                return
            
            if o < n and c < n and o >= c:
                dfs(o + 1, c, cur + "(")

                dfs(o, c + 1, cur + ")")
            
            if o == n and c < n:
                dfs(o, c + 1, cur + ")")
            
        
        dfs(1, 0, "(")
        return res