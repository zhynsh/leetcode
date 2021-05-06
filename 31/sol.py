#https://leetcode-cn.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1;
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                index = i;
        if index > -1:
            tempind = index + 1;
            for i in range(index + 2, len(nums)):
                if nums[i] > nums[index] and nums[i] < nums[tempind]:
                    tempind = i;
            nums[index], nums[tempind] = nums[tempind], nums[index];
            for i in range(0, len(nums) - index - 1):
                for j in range(index + 1, len(nums) - i - 1):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j];
        else:
            nums.reverse();