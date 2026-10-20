class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        running1 = 1
        running2 = 1
        for i in range(len(nums)):
            res[i] *= running1
            running1 *= nums[i]             
            # res[i] *= running1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= running2
            running2 *= nums[i]
        return res