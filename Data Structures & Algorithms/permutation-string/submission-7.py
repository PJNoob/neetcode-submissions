# First check if s1 is longer than s2. If it is, a permutation of s1 cannot possibly exist inside s2, so return False.
# Create two arrays of size 26, map1 and map2, where each index represents a lowercase English character from a to z.
# Build map1 using s1, where each position stores the frequency of that character in s1.
# Build map2 using the first len(s1) characters of s2, creating the first sliding window with the same size as s1.
# Compare map1 and map2. If they're equal, the current window contains exactly the same characters with the same frequencies, meaning it is a permutation of s1.
# Slide the window through s2 one character at a time.
# Add the new right-side character to map2 because it has entered the window.
# Remove the old left-side character from map2 because it has left the window.
# Compare the two frequency arrays again after every window movement.
# If the frequency arrays match, return True because the current window is a permutation of s1.
# If no window matches, return False.

# Complexity:
# Time: O(n) because you traverse s2 once. The comparison map1 == map2 is technically O(26), which is constant.
# Space: O(1) because both frequency arrays always contain exactly 26 elements.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = [0]*26
        map2 = [0]*26

        for c in s1:
            map1[ord(c) - ord('a')] += 1

        for c in s2[:len(s1)]:
            map2[ord(c) - ord('a')] += 1

        if map1 == map2:
            return True

        for right in range(len(s1), len(s2)):

            left = right - len(s1)

            map2[ord(s2[right]) - ord('a')] += 1
            map2[ord(s2[left]) - ord('a')] -= 1

            if map1 == map2:
                return True

        return False

