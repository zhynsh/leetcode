class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort();
        out = [];
        for i in range(1, len(nums) - 1):
            if (nums[i] == 0 and nums[i] == nums[i - 1] and nums[i] == nums[i + 1]):
                out.append([0, 0, 0]);
                break;
            if nums[i] > 0:
                break;
        for i in range(1, len(nums) - 1):
            if i > 1 and nums[i] >= 0 and nums[i] == nums[i - 1]:
                continue;
            if i < len(nums) - 2 and nums[i] < 0 and nums[i] == nums[i + 1]:
                continue;
            left = i - 1;
            right = i + 1;
            while left >= 0 and right < len(nums):
                if (left > 0 and nums[left - 1] == nums[left]):
                    left = left - 1;
                    continue;
                if (right < len(nums) - 1 and nums[right + 1] == nums[right]):
                    right = right + 1;
                    continue;
                if (nums[left] + nums[i] + nums[right]) < 0:
                    right = right + 1;
                    continue;
                if (nums[left] + nums[i] + nums[right]) > 0:
                    left = left - 1;
                    continue;
                if [nums[left], nums[i], nums[right]] != [0, 0, 0]:
                    out.append([nums[left], nums[i], nums[right]]);
                if (nums[left] == 0):
                    flag = 1;
                if left > 0 and right < len(nums) - 1:
                    if (nums[left] - nums[left - 1] < nums[right + 1] - nums[right]):
                        left = left - 1;
                    else:
                        right = right + 1;
                elif left > 0:
                    left = left - 1;
                elif right < len(nums) - 1:
                    right = right + 1;
                else:
                    break;
        return out;