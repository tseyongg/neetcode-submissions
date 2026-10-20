class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]
        for a, b in intervals:
            if out[-1][1] >= a:
                out[-1][1] = max(out[-1][1], b)
            else:
                out.append([a, b])
        return out