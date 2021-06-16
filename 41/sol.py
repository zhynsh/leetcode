#https://leetcode-cn.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        if 1 not in nums:
            return 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] >= 0 and nums[i + 1] > nums[i] + 1:
                return nums[i] + 1
        if nums[-1] >= 0:
            return nums[-1] + 1
        return 1
