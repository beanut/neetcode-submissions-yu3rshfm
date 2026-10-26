class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = Counter(hand)

        for card in sorted(counts):
            cnt = counts[card]
            if cnt > 0:
                for n in range(card, card + groupSize):
                    if n not in counts or counts[n] <= 0:
                        return False
                    counts[n] -= cnt
        return True
        