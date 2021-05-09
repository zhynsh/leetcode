#https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            for i in range(0, len(nums)):
                if target == nums[len(nums) - 1 - i]:
                    return len(nums) - 1 - i;
                elif target > nums[len(nums) - 1 - i]:
                    return -1;
                elif nums[0] <= nums[len(nums) - 1 - i]:
                    return -1;
        elif target == nums[0]:
            return 0;
        else:
            for i in range(1, len(nums)):
                if target == nums[i]:
                    return i;
                elif target < nums[i]:
                    return -1;
                elif nums[0] >= nums[i]:
                    return -1;
        return -1;