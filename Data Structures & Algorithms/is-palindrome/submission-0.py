class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for char in s:
            if char.isalnum():
                news += char.lower()
        l, r = 0, len(news) - 1
        while l < r:
            if not news[l] == news[r]:
                return False
            l += 1
            r -= 1
        return True

