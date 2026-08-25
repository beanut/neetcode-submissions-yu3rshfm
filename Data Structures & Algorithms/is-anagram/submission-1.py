from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        d = Counter(t)

        return c == d
        