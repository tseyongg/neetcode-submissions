class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            left, right = heights[l], heights[r]
            vol = (r - l) * min(left, right)
            best = max(best, vol)
            if left > right:
                r -= 1
            else:
                l += 1
        return best