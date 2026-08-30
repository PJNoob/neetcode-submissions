# Create a set charSet to keep track of the unique characters currently inside our window.
# Use two pointers, where left represents the beginning of the current substring and right represents the end of the current substring.
# Start left at 0 and move right through the string one character at a time.
# Check whether s[right] is already in the set.
# If it is not present, add it to the set because the current substring still contains unique characters.
# If it is already present, we have found a duplicate, so the current window is invalid.
# Remove characters from the left side using the while loop until the duplicate character is removed.
# Move left forward each time a character is removed, effectively shrinking the window from the left.
# Add the current s[right] to the set once the window contains no duplicate.
# Calculate the current window length using right - left + 1.
# Update result if the current window is longer than the longest substring found so far.
# Continue moving right until the entire string has been processed.
# Return result, which is the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result