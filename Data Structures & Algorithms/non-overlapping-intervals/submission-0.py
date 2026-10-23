class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        out = [intervals[0]]

        for a, b in intervals[1:]:
            if out[-1][1] > a:
                continue
            else:
                out.append([a,b])
        return len(intervals) - len(out)