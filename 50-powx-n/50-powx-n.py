class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x
        
        
        """ans = 1.0
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
        return ans"""