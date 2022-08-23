import queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket Sort -> TC: O(n)
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        
        
        
        
        
        
        
        #Heap -> TC: O(klogn)
        """if k == len(nums):
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
        return ans"""
        