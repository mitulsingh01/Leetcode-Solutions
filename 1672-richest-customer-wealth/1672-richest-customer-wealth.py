class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxMoney = 0
        for i in range(len(accounts)):
            maxMoney = max(maxMoney, sum(accounts[i]))
        return maxMoney