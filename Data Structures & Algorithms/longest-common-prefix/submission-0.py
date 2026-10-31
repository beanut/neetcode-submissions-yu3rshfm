class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = 0

        minlen = min(map(lambda s: len(s), strs))
        stop = False
        while r < minlen:
            for i, s in enumerate(strs):
                if i > 0 and not strs[i][r] == strs[i - 1][r]:
                    stop = True
                    break
            if stop:
                break
            r += 1

        return strs[0][:r]