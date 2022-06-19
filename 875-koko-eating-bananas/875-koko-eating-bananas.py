class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end
        while start <= end:
            mid = start + (end-start)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                start = mid + 1
        return res
            