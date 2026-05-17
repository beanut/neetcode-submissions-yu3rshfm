class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = Counter(s)
        tcount = Counter(t)

        return scount == tcount