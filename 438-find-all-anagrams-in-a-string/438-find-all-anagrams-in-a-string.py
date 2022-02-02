class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans
        pmap, smap = {}, {}
        #for first substring
        for i in range(len(p)):
            pmap[p[i]] = 1 + pmap.get(p[i], 0)
            smap[s[i]] = 1 + smap.get(s[i], 0)
        ans = [0] if smap == pmap else []
        l = 0
        for r in range(len(p), len(s)):
            smap[s[r]] = 1 + smap.get(s[r], 0)
            smap[s[l]] -= 1
            
            if smap[s[l]] == 0:
                smap.pop(s[l])
            l += 1
            if smap == pmap:
                ans.append(l)
                
        return ans