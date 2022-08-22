class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap, res = [], []
        for x, y in points:
            minHeap.append([x**2 + y**2]+[x,y])
        heapq.heapify(minHeap)
        while k:
            res.append(heapq.heappop(minHeap)[1:])
            k -= 1
        return res