class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 0
        currMax, globalMax = 0, 0
        while r < len(nums):
            if nums[r] == 1:
                currMax += 1
                r += 1
                globalMax = max(globalMax, currMax)
            else:
                l = r
                r += 1
                currMax = 0
        return globalMax