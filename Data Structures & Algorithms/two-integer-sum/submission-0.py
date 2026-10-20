class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            desired = target - n
            if desired in d:
                return [d[desired], i]
            d[n] = i
