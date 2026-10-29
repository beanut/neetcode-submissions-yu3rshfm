class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(n) -> int:
            if n == 0:
                return mapping[0]
            place = 1
            res = 0

            while n:
                curDigit = n % 10
                res += mapping[curDigit] * place
                place *= 10
                n //= 10

            return res

        return sorted(nums, key=lambda x: mapped(x))
