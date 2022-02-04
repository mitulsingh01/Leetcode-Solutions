class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        mapp = {}
        count = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                count -= 1
            else:
                count += 1
                
            if count == 0:
                maxLen = i + 1
                
            if count in mapp:
                maxLen = max(maxLen, i-mapp[count])
            else:
                mapp[count] = i
        return maxLen