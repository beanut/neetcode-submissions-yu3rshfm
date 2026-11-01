class Solution:
    def decodeString(self, s: str) -> str:
        # 12:04
        res = []
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                cur = ""
                while stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                reps = 0
                place = 1
                while stack and stack[-1].isdigit():
                    reps += place * int(stack.pop())
                    place *= 10
                stack.append(cur * reps)
        
        return "".join(stack)


