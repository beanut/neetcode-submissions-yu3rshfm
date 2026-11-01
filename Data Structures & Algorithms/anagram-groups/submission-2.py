class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            f = [0] * 26
            for c in s:
                f[ord(c) - ord('a')] += 1
            res[tuple(f)].append(s)
        
        return list(res.values())