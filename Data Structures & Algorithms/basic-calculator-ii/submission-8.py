class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        l = 0
        while l < len(s):
            r = l
            while r < len(s) and s[r] not in ["+", "-", "*", "/"]:
                r += 1
            num = int(s[l:r])
            if stack and stack[-1] in ["*", "/"]:
                op = stack.pop()
                prev = stack.pop()
                if op == "*":
                    stack.append(num * prev)
                else:
                    stack.append(prev // num)
            else:
                stack.append(num)
            if r < len(s):
                stack.append(s[r])
            r += 1
            l = r

        stack.reverse()
        while len(stack) >= 2:
            num2 = stack.pop()
            op = stack.pop()
            num1 = stack.pop()
            if op == "+":
                stack.append(num1 + num2)
            else:
                stack.append(num2 - num1)
        
        return stack[0]

