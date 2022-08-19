import queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        mp = {}
        for ele in nums:
            if ele not in mp:
                mp[ele] = 0
            mp[ele] += 1
        heap = queue.PriorityQueue()
        for x in mp:
            heap.put([-mp[x], -x])
        ans = [0]*k
        for i in range(k):
            ans[i] = -heap.get()[1]
        ans.sort()
        return ans
        