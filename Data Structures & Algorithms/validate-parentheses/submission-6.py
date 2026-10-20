class Solution:
    def isValid(self, s: str) -> bool:
        b = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in b.values():
                stack.append(char)
            elif char in b.keys():
                if stack and stack[-1] == b[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False