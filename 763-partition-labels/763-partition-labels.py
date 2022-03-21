class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = {} #last  index
        for i, c in enumerate(s):
            mapp[c] = i
        res, size, end = [], 0, 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, mapp[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res