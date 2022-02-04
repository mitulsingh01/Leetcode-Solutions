class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        index = self.binarySearch(nums, l, r, target)
        return index
    
    def binarySearch(self, arr, l, r, x):
  
        # Check base case
        if r >= l:

            mid = l + (r - l) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid-1, x)

            # Else the element can only be present
            # in right subarray
            else:
                return self.binarySearch(arr, mid + 1, r, x)

        else:
            # Element is not present in the array
            return -1