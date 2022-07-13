class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, lcs = set(nums), 0
        for num in s:
            if num - 1 in s: continue
            streak = 1
            while num + streak in s: streak += 1
            lcs = max(lcs, streak)
        return lcs