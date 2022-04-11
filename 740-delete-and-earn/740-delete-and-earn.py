class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]]= 1
                
        nums = sorted(list(set(nums)))
        
        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = earn2 + curEarn
                earn1 = temp
        return earn2