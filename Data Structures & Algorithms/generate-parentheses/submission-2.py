class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = []

        def backtrack(o: int, c: int):
            if o == c == n:
                res.append(''.join(cur))
                return
            
            if o < n:
                cur.append('(')
                backtrack(o + 1, c)
                cur.pop()
            
            if o > c:
                cur.append(')')
                backtrack(o, c + 1)
                cur.pop()
        
        backtrack(0, 0)
        return res