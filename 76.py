# Sliding window, TIme - O(n), Space - O(26)
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = defaultdict(int)
        res = ""
        l = 0
        have = 0

        for c in t:
            count[c] += 1
        need = len(count)

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1

                if count[s[r]] == 0:
                    have += 1 

            while have == need:
                if len(res) > (r - l + 1) or not res: 
                    res = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1

                    if count[s[l]] == 1:
                        have -= 1
                l += 1    

        return res