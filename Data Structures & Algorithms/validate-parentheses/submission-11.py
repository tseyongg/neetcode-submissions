class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", ")":"(", "]":"["}
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != d[char]:
                    return False
        return not stack