class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = defaultdict(lambda: [0, 0])

        # note: python dict preserves insertion order
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = [i, i]
            else:
                chars[c][1] = i

        merged = []
        for start, end in chars.values():
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])
        
        return list(map(lambda x: x[1] - x[0] + 1, merged))
        
        
