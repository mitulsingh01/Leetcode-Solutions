class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ele = 0, 0
        for number in nums:
            if count == 0:
                ele = number
            count = count + 1 if ele == number else count - 1
        return ele
            