# Original sol (expand around center), Time - O(n^2), Space - O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        ans = s[0]
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr = s[i-1] + s[i]
                x = i-2
                y = i+1
                
                while x > -1 and y < len(s) and s[x] == s[y]:
                    curr = s[x] + curr + s[y]
                    x -= 1
                    y += 1
                
                if len(curr) > len(ans):
                    ans = curr
            
            if i < len(s) - 1 and s[i-1] == s[i+1]:
                curr = s[i-1] + s[i] + s[i+1]
                x = i-2
                y = i+2

                while x > -1 and y < len(s) and s[x] == s[y]:
                    curr = s[x] + curr + s[y]
                    x -= 1
                    y += 1
                
                if len(curr) > len(ans):
                    ans = curr
        
        return ans
    
# More elegant (expand around center), Time - O(n^2), Space - O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        ans = s[0]

        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        
        for i in range(len(s)):
            even = expand(i, i)
            odd = expand(i, i+1)

            if len(even) > len(ans):
                ans = even
            if len(odd) > len(ans):
                ans = odd
        
        return ans