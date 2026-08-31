# Create freqMap to keep track of how many times each character appears inside the current window.
# Use left and right pointers to represent the current sliding window.
# Move right through the string and add s[right] to the frequency map.
# Keep track of maxf, which represents the highest frequency of any single character inside the current window.
# Calculate how many replacements are required using (window length) - maxf.
# Why this works: the most frequent character can remain unchanged, and every other character needs to be replaced with that character.
# If replacements required are greater than k, the current window is invalid, so remove s[left] from the frequency map and move left forward.
# Update maxLength with the size of the current valid window.
# Move right forward and continue expanding the window.
# Return maxLength once the entire string has been processed.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        left = 0
        right = 0
        maxLength = 0
        maxf = 0

        while right < len(s):
            freqMap[s[right]] += 1

            maxf = max(maxf, freqMap[s[right]])

            while (right - left + 1) - maxf > k:
                freqMap[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength