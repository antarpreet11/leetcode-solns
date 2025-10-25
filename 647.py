# Expand around center, Time - O(n^2), Space - O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0

        def expand(l: int, r: int) -> None:
            nonlocal ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return ans