# Time - O(amount * len(coins)), Space - O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [amount + 1] * (amount + 1)
        result[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    result[a] = min(1 + result[a - c], result[a])
        return result[amount] if result[amount] != amount + 1 else -1 