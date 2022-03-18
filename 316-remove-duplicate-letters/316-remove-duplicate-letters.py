class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dict = {}
        res = []
        for ind, char in enumerate(s):
            dict[char] = ind
        
        for ind, ch in enumerate(s):
            if ch not in res:
                while res and ind < dict[res[-1]] and ch < res[-1]:
                    res.pop()
                res.append(ch)
        
        return "".join(res)
        
            
        