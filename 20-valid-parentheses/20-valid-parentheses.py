class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '{' or item == '[' or item == '(':
                stack.append(item)
            else:
                if not len(stack): return False
                ch = stack.pop()
                if((item == ')' and ch == '(') or  (item == ']' and ch == '[') or (item == '}' and ch == '{')):
                    continue
                else:
                    return False
        return len(stack) == 0