# Time - O(n), Space - O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, nums[0]

        for i in range(1, len(nums)):
            temp = max((one + nums[i]), two)
            one = two
            two = temp

        return two