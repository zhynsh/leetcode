#https://leetcode-cn.com/problems/single-number-ii/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort();
        if len(nums) < 2:
            return nums[0];
        i = 1;
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                return nums[i - 1];
            i = i + 3;
        return nums[len(nums) - 1];
