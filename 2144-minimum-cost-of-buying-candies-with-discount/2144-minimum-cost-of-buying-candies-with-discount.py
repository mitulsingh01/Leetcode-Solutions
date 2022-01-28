class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        minSum = 0
        added = 0
        for i in cost[::-1]:
            if added < 2:
                minSum += i
                added += 1
            elif added == 2:
                added = 0
        return minSum