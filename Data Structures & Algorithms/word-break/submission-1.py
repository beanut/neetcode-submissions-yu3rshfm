class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        sizes = set(list(map(lambda x : len(x), wordDict)))

        failed = set() # Strings that lead to false

        def dfs(start: int) -> bool:
            if start == len(s):
                return True

            if start in failed:
                return False

            for size in sizes:
                end = start + size
                if end <= len(s) and s[start:end] in words:
                    if dfs(end):
                        return True
            
            failed.add(start)
            return False

        return dfs(0)