class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set(nums)
        return (sum(nums) - sum(dup))//(len(nums)-len(dup))