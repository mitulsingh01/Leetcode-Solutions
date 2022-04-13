class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        
        maxDP = [i for i in nums]
        minDP = [i for i in nums]
        
        for i in range(1, len(nums)):
            if maxDP[i-1] > 0:
                maxDP[i] += maxDP[i-1]
            if minDP[i-1] < 0:
                minDP[i] += minDP[i-1]
            
        return max(max(maxDP), sum(nums) - min(minDP))