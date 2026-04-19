# Time - O(n), Space - O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
        return False

# Time - O(n), Space - O(n)   
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)