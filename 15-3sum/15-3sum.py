class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo, hi = i + 1, len(nums)-1
                summ = 0 - nums[i]
                
                while lo < hi:
                    if nums[lo] + nums[hi] == summ:
                        ans.append([nums[i], nums[lo], nums[hi]])
                        
                        while lo < hi and nums[lo] == nums[lo + 1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]: hi -= 1
                        
                        lo += 1
                        hi -= 1
                        
                    elif nums[lo] + nums[hi] < summ:
                        lo += 1
                    else:
                        hi -= 1
        return ans