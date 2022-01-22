class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        minSum = 0
        i = len(cost) - 1
        while i >= 0:
            if i >= 0:
                minSum += cost[i]
                i -= 1
            if i >= 0:
                minSum += cost[i]
                i -= 1
            i -= 1
        return minSum