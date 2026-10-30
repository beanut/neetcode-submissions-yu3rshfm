class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # [1,2,2,3,3]

        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            s = people[r]
            if l < r and s + people[l] <= limit:
                s += people[l]
                l += 1
            count += 1
            r -= 1

        return count