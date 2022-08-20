class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mapp = {}
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = 0
            mapp[nums[i]] += 1
        count = 0
        if k == 0:
            for i in mapp.values():
                if i > 1:
                    count += 1
        else:
            for i in mapp:
                if i + k in mapp:
                    count += 1
        return count