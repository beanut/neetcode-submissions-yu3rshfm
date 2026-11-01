class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for dir in path:
            if len(dir) == 0 or dir == '.':
                continue
            if dir != '..':
                stack.append(dir)
            elif len(stack) >= 1:
                stack.pop()
        
        return "/" + "/".join(stack)