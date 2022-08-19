class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for r in range(len(nums)):
            heappush(minHeap, nums[r])
            if len(minHeap) > k:
                heappop(minHeap)
        return heappop(minHeap)