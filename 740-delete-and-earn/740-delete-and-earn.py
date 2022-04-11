class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if  not nums:
            return 0

        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i-2], dp[i-1])

        return dp[len(freq)-1]
        
        
        """count = {}
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
        return earn2"""
        
        