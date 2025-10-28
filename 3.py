# Time - O(n), Space - O(m), m - num of unique chars
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numChars = defaultdict(int)
        l, r = 0, 0
        maxL = 0

        while r < len(s):
            numChars[s[r]] += 1

            while numChars[s[r]] > 1 and l <= r:
                numChars[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
            r += 1
        
        return maxL