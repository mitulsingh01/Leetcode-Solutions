class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        length = sum(nums)//4
        sides = [0]*4
        
        if sum(nums)/4 != length:
            return False
        nums.sort(reverse=True)
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(4):
                if sides[j] + nums[i] <= length:
                    sides[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= nums[i]
            return False
        return backtrack(0)
        
        
        