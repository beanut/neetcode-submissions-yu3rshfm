class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets = list(filter(lambda x: 
            x[0] <= target[0] and x[1] <= target[1] and x[2] <= target[2]
        , triplets))

        return all(any(t[i] == target[i] for t in triplets) for i in range(3))



        