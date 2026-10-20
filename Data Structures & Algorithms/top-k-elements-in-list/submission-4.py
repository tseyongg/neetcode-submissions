class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        newlist = list(d.items())
        newlist.sort(key = lambda x:x[1], reverse = True)
        out = []
        for a, b in newlist[:k]:
            out.append(a)
        return out