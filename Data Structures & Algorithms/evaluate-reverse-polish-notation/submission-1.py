class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # res = stack[0]
        for tk in tokens:
            if tk == "+":
                stack[-2] = str(int(stack[-2]) + int(stack[-1]))
                stack.pop()
            elif tk == "-":
                stack[-2] = str(int(stack[-2]) - int(stack[-1]))
                stack.pop()
            elif tk == "*":
                stack[-2] = str(int(stack[-2]) * int(stack[-1]))
                stack.pop()
            elif tk == "/":
                stack[-2] = str(int(int(stack[-2]) / int(stack[-1])))
                stack.pop()
            else:
                stack.append(tk)
        
        return int(stack[0])