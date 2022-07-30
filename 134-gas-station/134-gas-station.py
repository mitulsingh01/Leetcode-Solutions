class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        totalGas = res = 0
        for i in range(len(cost)):
            totalGas += (gas[i]-cost[i])
            if totalGas < 0:
                totalGas = 0
                res = i + 1
            
        return res