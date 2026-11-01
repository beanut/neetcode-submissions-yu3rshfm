class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            skip = False
            """
            neg, pos: no collision
            pos, neg: collides
            """
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                    continue
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                skip = True
                break
            if not skip:
                stack.append(a)
        
        return stack
                    

