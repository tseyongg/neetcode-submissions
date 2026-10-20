class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        for n in numset:
            if n-1 not in numset:
                counter = 1
                while n + 1 in numset:
                    counter += 1
                    n += 1
                maxcount = max(maxcount, counter)
        return maxcount

