class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            target3 = target - nums[i]
            for j in range(i+1, n):
                target2 = target3 - nums[j]
                front, back = j+1, n-1
                while front < back:
                    twoSum = nums[front] + nums[back]
                    if twoSum < target2: 
                        front += 1
                    elif twoSum > target2: 
                        back -= 1
                    else:
                        quad = [0]*4
                        quad[0] = nums[i]
                        quad[1] = nums[j]
                        quad[2] = nums[front]
                        quad[3] = nums[back]
                        res.add(tuple(sorted((quad[0], quad[1], quad[2],quad[3]))))
                        
                        while (front < back and nums[front] == quad[2]): 
                            front += 1
                        while (front < back and nums[back] == quad[3]):
                            back -= 1
                while (j + 1 < n and nums[j + 1] == nums[j]):
                    j += 1
            while (i + 1 < n and nums[i + 1] == nums[i]): 
                i += 1
        return res

                    
                
        
        
        
        
        
        
        
        """# loop for first num, n times
        for i in range(len(nums)):   
            # skip duplication
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # skip uneccesary case
            if nums[i] * 4 > target:
                break

            # loop for second number, n times
            for j in range(i + 1, len(nums) - 2):
                
                # skip duplication
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # skip uneccesary case
                if nums[j] * 3 > target - nums[i]:
                    break

                # search for last 2 nums, same as 2Sum/3Sum problem
                l, r = j + 1, len(nums) - 1

                while l < r:
                    
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r = r - 1
                    elif s < target:
                        l = l + 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l, r = l + 1, r - 1
            
        return res"""