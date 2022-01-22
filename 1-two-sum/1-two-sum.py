class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        dictnum = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dictnum:
                return [dictnum[diff], i]
            else:
                dictnum[n] = i
        return
    
        