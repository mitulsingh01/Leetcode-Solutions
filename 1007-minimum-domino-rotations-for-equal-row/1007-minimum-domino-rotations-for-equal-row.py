class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missingT, missingB = 0, 0
            for i in range(len(tops)):
                if not (tops[i] == target or bottoms[i] == target):
                    break
                if tops[i] != target:
                    missingT += 1
                if bottoms[i] != target:
                    missingB += 1
                if i == len(tops) - 1:
                    return min(missingT, missingB)
        return -1
        