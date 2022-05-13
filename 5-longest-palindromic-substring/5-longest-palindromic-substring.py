class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Neetcode Answer
        res = ""
        resLen = 0
        for i in range(len(s)):
            #for odd length string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            #for even length string 
            l , r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        return res"""
        #DP solution
        ans = ""
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            ans = s[i]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        
                        if len(ans) < len(s[i:j+1]):
                            ans = s[i:j+1]
        return ans