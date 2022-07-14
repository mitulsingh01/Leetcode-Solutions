class Solution:
    def searchRange(self, nums: List[int], ele: int) -> List[int]:
        def leftBS(nums, ele):
            start, end = 0, len(nums)-1
            while start <= end:
                mid = start + (end-start)//2
                if ele > nums[mid]:
                    start = mid + 1
                else:
                    end = mid-1
            return start
        def rightBS(nums, ele):
            start, end = 0, len(nums)-1
            while start <= end:
                mid = start + (end-start)//2
                if ele >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid-1
            return end
        left, right = leftBS(nums, ele), rightBS(nums, ele)
        return [left, right] if left <= right else [-1, -1]