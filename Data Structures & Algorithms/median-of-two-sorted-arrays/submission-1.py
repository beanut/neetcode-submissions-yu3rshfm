class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # A is the shorter array
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # partition is right
                if total % 2 == 1:
                    # odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # partition not right
            if not Aleft <= Bright:
                # need to shrink A part; expand B part
                # use binary search for this
                r = i - 1
            elif not Bleft <= Aright:
                # need to expand A part; shrink B part
                # A's left partition is too small. Since Bleft > Aright,
                # the current partition i is invalid, and every partition <= i
                # is also invalid. Skip them all and search strictly to the right.
                # i.e. we're 100% sure i can't be the mid
                l = i + 1

