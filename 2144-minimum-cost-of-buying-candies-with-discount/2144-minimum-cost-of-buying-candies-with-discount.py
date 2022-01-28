class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        minSum = 0
        n = len(cost)
        for i in range(n):
            #free index
            if (i % 3 == 2):
                continue
            else:
                minSum += cost[i]
        return minSum