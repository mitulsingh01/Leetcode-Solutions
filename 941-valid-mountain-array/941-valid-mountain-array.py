class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)   
        start =  0
        #Walk up
        while start+1 < length and arr[start] < arr[start+1]:
            start += 1
        #Peak can't be first or last
        if start == 0 or start == length-1:
            return False
        #Walk Down
        while start+1 < length and arr[start] > arr[start+1]:
            start += 1
        return start == length-1