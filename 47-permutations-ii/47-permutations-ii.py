class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        mapp = {n:0 for n in nums}
        
        for n in nums:
            mapp[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[::])
                return
            
            for n in mapp:
                #do
                if mapp[n] > 0:
                    perm.append(n)
                    mapp[n] -= 1
                    
                    #recur
                    dfs()
                    
                    #undo 
                    mapp[n] += 1
                    perm.pop()
                
        dfs()
        return res