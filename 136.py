# Time - O(n), Space - O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num #XOR
        return res