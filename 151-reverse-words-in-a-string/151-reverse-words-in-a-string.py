class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s)-1
        temp = ""
        ans = ""
        
        while l <= r:
            ch = s[l]
            if ch != ' ':
                temp += ch
            elif ch == " ":
                if temp != "":
                    if ans != "":
                        ans = temp + ch + ans
                    else:
                        ans = temp
                    temp = ""
            l += 1
        if temp != "":
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp
        return ans