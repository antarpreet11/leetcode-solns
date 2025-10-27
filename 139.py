# DP Bottom Up, Time - O(n * m * t) n = len(s), m = len(wordDict), t = len(longestWord), Space - O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:].startswith(word):
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]