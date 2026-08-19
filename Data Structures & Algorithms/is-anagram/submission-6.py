class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        arr1 = [0]*27
        arr2 = [0]*27

        for i in range(len(s)):
            arr1[ord(s[i])-ord('a')] += 1

        for i in range(len(t)):
            arr2[ord(t[i])-ord('a')] += 1

        if arr1 == arr2:
            return True
        else:
            return False

            
        