class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                a -= 1
            else:
                A[write_index] = B[b]
                b -= 1

            write_index -= 1
        
        
        """for i in range(n):
            nums1.pop()
        nums1 += nums2
            
        gap = ceil((m + n) / 2)
        
        gap1count = 0
        
        while gap > 0:
            i = 0
            j = i + gap
            while j < m + n:
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
                i += 1
                j += 1
            gap = (gap + 1) // 2
            
            if gap == 1:
                gap1count += 1
                if gap1count > 1: break
                
        return nums1"""