class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """nums.sort()
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
        return l"""
        
        for num in nums:          
            # if the position is already marked
            # then the index is the duplicate
            if nums[abs(num)-1] < 0:
                return abs(num)
            nums[abs(num)-1] *= -1
        
        """slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:  # Meeting Point
                break

        left = 0  # Pointer to detect the repeating element

        while True:
            slow = nums[slow]
            left = nums[left]
            if slow == left:
                return slow"""
                