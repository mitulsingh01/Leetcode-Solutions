class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n
        if nn < 0:
            nn *= -1
        
        while nn > 0:
            if nn % 2 == 1:
                ans *= x
                nn -= 1
            else:
                x *= x
                nn /= 2
        if n < 0:
            ans = 1.0/ans
        return ans