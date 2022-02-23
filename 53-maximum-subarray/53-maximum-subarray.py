class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's ALgorithm
        if len(nums) < 1:
            return None
        currSum = 0
        globalSum = nums[0]
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            globalSum = max(currSum, globalSum)
        return globalSum