# Handle the empty t case by immediately returning "" because there is nothing to search for.
# Create countMap to store how many times each character is required from t.
# Create window to store the frequency of characters currently inside the sliding window of s.
# Set need to the number of unique characters in t, because we need to completely satisfy each unique character's frequency requirement.
# Set have = 0 to track how many unique characters currently have their required frequency satisfied inside the window.
# Start with left = 0 and right = 0, meaning the window initially starts empty.
# Move right forward and add each character to window.
# If the newly added character is required by t and its window frequency exactly reaches the required frequency, increase have.
# When have == need, the current window contains everything required by t, so it is a valid window.
# While the window is valid, try shrinking it from the left because the goal is to find the smallest valid window.
# Before removing anything, check whether the current window is smaller than the best window found so far, and save it if it is.
# Remove s[left] from window and move left forward.
# If removing that character causes its frequency to become less than what t requires, decrease have, meaning the window is no longer valid.
# Once the window becomes invalid, stop shrinking and continue moving right to find another valid window.
# At the end, return the smallest window stored in res, or "" if no valid window was found.

# Expand → Become valid → Shrink as much as possible → Become invalid → Expand again

# Time: O(|s| + |t|) — each character is added to and removed from the window at most once.
# Space: O(|s| + |t|) in the general case because the dictionaries can contain characters from the strings. With a fixed-size alphabet, it can be considered O(1).

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countMap = defaultdict(int)
        window = defaultdict(int) #window

        for c in t:
            countMap[c] += 1

        have = 0
        need = len(countMap)

        left,right = 0,0

        res = [-1,-1]
        resLen = float("infinity")

        while right < len(s):
            c = s[right]
            window[c] += 1

            if c in countMap and countMap[c] == window[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                
                window[s[left]] -= 1

                if s[left] in countMap and countMap[s[left]] > window[s[left]]:
                    have -= 1

                left += 1

            right += 1

        l,r = res
        return s[l: r + 1] if resLen != float("infinity") else "" 