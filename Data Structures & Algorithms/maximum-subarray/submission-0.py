class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        largest_sum = nums[0]

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n

            largest_sum = max(largest_sum, curr_sum)

        return largest_sum