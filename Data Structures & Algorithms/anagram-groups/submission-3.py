class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorteds = "".join(sorted(s))
            if sorteds in d:
                d[sorteds].append(s)
            else:
                d[sorteds] = [s,]
        return list(d.values())

