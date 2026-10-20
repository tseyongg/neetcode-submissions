class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s (str): Input string
        
        Returns:
            int: Length of longest substring without duplicates
        """
        # Handle edge case: empty string
        if not s:
            return 0
        
        # Dictionary to store the most recent index of each character
        char_index_map = {}
        
        # Left pointer of the sliding window
        left = 0
        max_length = 0
        
        # Right pointer iterates through the string
        for right in range(len(s)):
            current_char = s[right]
            
            # If character is already seen and is within current window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move left pointer to position after the duplicate character
                left = char_index_map[current_char] + 1
            
            # Update the most recent index of current character
            char_index_map[current_char] = right
            
            # Update maximum length found so far
            max_length = max(max_length, right - left + 1)
        
        return max_length
