class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        map1 = defaultdict(int)
        map2 = defaultdict(int) #window

        for c in t:
            map1[c] += 1

        have = 0
        need = len(map1)

        left,right = 0,0

        res = [-1,-1]
        resLen = float("infinity")

        while right < len(s):
            c = s[right]
            map2[c] += 1

            if c in map1 and map1[c] == map2[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                
                map2[s[left]] -= 1

                if s[left] in map1 and map1[s[left]] > map2[s[left]]:
                    have -= 1

                left += 1

            right += 1

        l,r = res
        return s[l: r + 1] if resLen != float("infinity") else "" 