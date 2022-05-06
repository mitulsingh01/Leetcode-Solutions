class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = []
        
        for i in s:
            if count and count[-1][0] == i:
                count[-1][1] += 1
            else:
                count.append([i, 1])
                
            if count[-1][1] == k:
                count.pop()
        
        res = ""
        for char, freq in count:
            res += (char*freq)
        
        return res