from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        wanted = [0] * 26
        cur = [0] * 26

        windowSize = len(s1)

        # fill wanted
        for c in s1:
            idx = ord(c) - ord('a')
            wanted[idx] += 1
        
        # fill the first windowSize chars from s2 into cur
        l = 0
        r = 0
        while r < windowSize:
            c = s2[r]
            idx = ord(c) - ord('a')
            cur[idx] += 1
            r += 1

        if wanted == cur:
                return True

        while r < len(s2):
            if wanted == cur:
                return True

            incoming = s2[r]
            outgoing = s2[l]

            cur[ord(incoming) - ord('a')] += 1
            cur[ord(outgoing) - ord('a')] -= 1

            r += 1
            l += 1

            if wanted == cur:
                return True
        
        return False
            
        



