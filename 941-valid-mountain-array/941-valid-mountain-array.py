class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        start, end = 0, length-1
        while start+1 < length-1 and arr[start] < arr[start+1]:
            start += 1
        while end-1 > 0 and arr[end] < arr[end-1]:
            end -= 1
        return start == end