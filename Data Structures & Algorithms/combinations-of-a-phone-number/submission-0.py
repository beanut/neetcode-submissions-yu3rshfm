class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        cur = []

        def backtrack(idx: int):
            if len(digits) == 0:
                return
            if len(cur) == len(digits):
                res.append(''.join(cur.copy()))
                return
            
            for c in mapping[digits[idx]]:
                cur.append(c)
                backtrack(idx + 1)
                cur.pop()
        
        backtrack(0)
        return res
