class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f = [0] * 26

        for c in magazine:
            f[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            f[ord(c) - ord('a')] -= 1
            if f[ord(c) - ord('a')] < 0:
                return False

        return True