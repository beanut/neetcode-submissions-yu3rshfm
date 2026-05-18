class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            new = str(len(s)) + "#" + s
            res = res + new
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            lim = s.find("#")
            len = int(s[0:lim])
            res.append(s[lim + 1:lim + 1 +len])
            s = s[lim + 1 +len:]
        return res