class Solution:

    sizes = []

    def encode(self, strs: List[str]) -> str:
        ret = ""
        self.sizes = []
        for s in strs:
            self.sizes.append(len(s))
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        ptr = 0
        ret = []
        for size in self.sizes:
            cur = ""
            for i in range(ptr, size + ptr):
                cur += s[i]
                ptr += 1
            ret.append(cur)

        return ret
