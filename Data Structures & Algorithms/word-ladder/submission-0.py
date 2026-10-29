class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        q = deque([beginWord])
        visited = {beginWord}

        level = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                cur = q.popleft()
                if cur == endWord:
                    return level + 1
                for i, char in enumerate(cur):
                    for c in "qwertyuiopasdfghjklzxcvbnm":
                        if c != char:
                            newCur = cur[:i] + c + cur[i+1:]
                            if newCur in words and newCur not in visited:
                                q.append(newCur)
                                visited.add(newCur)
            level += 1
            
        return 0