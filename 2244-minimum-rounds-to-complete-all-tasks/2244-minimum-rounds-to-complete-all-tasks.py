class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mapp = Counter(tasks)
        count = 0
        
        for key, val in mapp.items():
            if mapp[key] == 1:
                return -1
            if mapp[key] % 3 == 0:
                count += mapp[key] // 3
            else:
                while (mapp[key] % 3 != 0) and (mapp[key] >= 2):
                    mapp[key] -= 2
                    count += 1
                count += mapp[key] // 3
        return count