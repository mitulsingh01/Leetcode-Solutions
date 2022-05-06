class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = []
        temp = 0
        for i in range(len(s)):
            if (len(count) > 0 and s[i] != count[-1][0]) or (len(count) == 0):
                count.append([s[i], 1])
            elif len(count) > 0 and s[i] == count[-1][0]:
                count[-1][1] += 1
                if count[-1][1] == k:
                    count.pop()
            
        ans = []
        for i in range(len(count)):
            while count[i][1] > 0:
                ans.append(count[i][0])
                count[i][1] -= 1
        return "".join(map(str, ans))