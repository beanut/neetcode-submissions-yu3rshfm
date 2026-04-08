class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        for c in s:
            stack.append(c)
            if len(stack) > 1:
                last = stack[-1]
                secondLast = stack[-2]
                if secondLast in brackets and last == brackets[secondLast]:
                    stack.pop()
                    stack.pop()

        
        if len(stack) == 0:
            return True
        return False