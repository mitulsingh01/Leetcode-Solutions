class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(i, sub):
            if i == len(s):
                res.append(sub)
                return
            #Digit Case
            if s[i].upper() == s[i].lower():
                backtrack(i+1, sub+s[i])
            #Alphabet Case
            else:
                backtrack(i+1, sub+s[i].upper())
                backtrack(i+1, sub+s[i].lower())
                
        backtrack(0, "")
        return res
        