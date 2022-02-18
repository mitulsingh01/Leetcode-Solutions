class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """char = {}
        char2 = {}
        for i in s:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1
        for i in t:
            if i in char2:
                char2[i] += 1
            else:
                char2[i] = 1
        return char == char2"""
        return sorted(s) == sorted(t)