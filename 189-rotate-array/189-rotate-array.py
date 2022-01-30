class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        #reversing the array
        reverse(0, n-1)  
        #reversing till k
        reverse(0, k-1)      
        #reversing from k to n
        reverse(k, n-1)
        
        