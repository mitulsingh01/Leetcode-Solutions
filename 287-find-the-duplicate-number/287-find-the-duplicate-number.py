class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
                
            if count <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l
                