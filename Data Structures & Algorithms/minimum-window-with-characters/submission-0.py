class Solution:
    def minWindow(self, s: str, t: str) -> str:
        psol = [-1, -1] # possible solution
        plen = 1001

        wanted = {}
        cur = {}

        # fill wanted with chars from t
        for c in t:
            wanted[c] = 1 + wanted.get(c, 0)

        satisfied = 0

        # wanted does not change after this point

        l = 0
        for r in range(len(s)):
            cr = s[r]
            if cr in wanted:
                cur[cr] = 1 + cur.get(cr, 0)
                if cur[cr] == wanted[cr]:
                    satisfied += 1

            while satisfied == len(wanted):
                if plen > r - l + 1:
                    plen = r - l + 1
                    psol = [l, r]
                
                cl = s[l]
                if cl in wanted:
                    cur[cl] -= 1
                    if cur[cl] < wanted[cl]:
                        satisfied -= 1
                l += 1

        if plen < 1001:
            return s[psol[0]:psol[1] + 1]
        else:
            return ""

