class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextBigger = {}

        for n in nums2:
            while stack and stack[-1] < n:
                prev = stack.pop()
                nextBigger[prev] = n
            stack.append(n)
        
        return list(map(lambda n: -1 if n not in nextBigger else nextBigger[n], nums1))