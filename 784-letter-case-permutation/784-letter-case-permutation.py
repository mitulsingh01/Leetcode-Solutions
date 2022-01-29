class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(s, i, sub, res):
            if i == len(s):
                res.append(sub)
                return
            #Digit Case
            if s[i].upper() == s[i].lower():
                backtrack(s, i+1, sub+s[i], res)
            #Alphabet Case
            else:
                backtrack(s, i+1, sub+s[i].upper(), res)
                backtrack(s, i+1, sub+s[i].lower(), res)
                
        backtrack(s, 0, "", res)
        return res
        