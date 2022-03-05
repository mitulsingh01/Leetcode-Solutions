class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans= [0]*len(nums)
        ind = 0
        for num in nums:
            res = ""
            temp = str(num)
            for i in range(len(temp)):
                res += str(mapping[int(temp[i])])
            ans[ind] = int(res)
            ind += 1
        res = list(zip(nums, ans))
        res = sorted(res, key=lambda x: x[1])
        res = [i[0] for i in res]
        return res