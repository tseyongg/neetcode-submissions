class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1:
            mid_idx = (len(nums) - 1) // 2
            if nums[mid_idx] > nums[len(nums) - 1]:
                nums = nums[mid_idx + 1:]
            else:
                nums = nums[:mid_idx + 1]
        return nums[0]