# Binary Search, Time - O(logN), Space - O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        res = nums[0]

        while i <= j:
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break

            k = (i + j) // 2
            res = min(res, nums[k])

            if nums[k] >= nums[i]:
                i = k + 1
            else:
                j = k - 1 
        return res