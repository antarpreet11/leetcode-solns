# Time - O(26 * n), Space - O(26)
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            charMap[s[r]] += 1

            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


# Time - O(n), Space - O(26)
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        res = 0
        l = 0
        maxF = 0

        for r in range(len(s)):
            charMap[s[r]] += 1
            maxF = max(maxF, charMap[s[r]])

            while (r - l + 1) - maxF > k:
                charMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res



