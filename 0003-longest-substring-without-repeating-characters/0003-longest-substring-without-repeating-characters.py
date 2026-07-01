class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Set to store characters in the current window
        left = 0          # Left pointer of the sliding window
        max_length = 0    # Variable to store the maximum length found

        # Iterate with the right pointer through the string
        for right in range(len(s)):
            # If the character at 'right' is already in our set,
            # it means we have a duplicate. We need to shrink the window
            # from the left until the duplicate is removed.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character at 'right' to the set
            char_set.add(s[right])
            
            # Update the maximum length found so far
            # The current length of the window is (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length