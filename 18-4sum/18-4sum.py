class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        # loop for first num, n times
        for i in range(len(nums) - 3):
            
            # skip duplication
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # skip uneccesary case
            if nums[i] * 4 > target:
                break

            # loop for second number, n times
            for j in range(i + 1, len(nums) - 2):
                
                # skip duplication
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # skip uneccesary case
                if nums[j] * 3 > target - nums[i]:
                    break

                # search for last 2 nums, same as 2Sum/3Sum problem
                l, r = j + 1, len(nums) - 1

                while l < r:
                    
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r = r - 1
                    elif s < target:
                        l = l + 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l, r = l + 1, r - 1
            
        return res