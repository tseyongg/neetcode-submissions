class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        
        # Iterate through the array, fixing the first element of each triplet
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if the smallest element is positive, 
            # no triplet can sum to zero
            if nums[i] > 0:
                break
            
            # Use two pointers to find pairs that sum to -nums[i]
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to continue searching
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    # Sum is too small, move left pointer right to increase sum
                    left += 1
                else:
                    # Sum is too large, move right pointer left to decrease sum
                    right -= 1
        
        return result