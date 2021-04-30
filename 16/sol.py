class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort();
        out = nums[0] + nums[1] + nums[2];
        for i in range(0, len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                if abs(out - target) > abs(nums[i] + nums[i + 1] + nums[i + 2] - target):
                    out = nums[i] + nums[i + 1] + nums[i + 2];
                break;
            if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] < target:
                if abs(out - target) > abs(nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] - target):
                    if i < len(nums) - 2:
                        out = nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2];
                continue;
            for j in range(i + 1, len(nums) - 1):
                if nums[i] + nums[j] + nums[j + 1] > target:
                    if abs(out - target) > abs(nums[i] + nums[j] + nums[j + 1] - target):
                        out = nums[i] + nums[j] + nums[j + 1];
                    break;
                if nums[i] + nums[j] + nums[len(nums) - 1] < target:
                    if abs(out - target) > abs(nums[i] + nums[j] + nums[len(nums) - 1] - target):
                        if j < len(nums) - 1:
                            out = nums[i] + nums[j] + nums[len(nums) - 1];
                    continue;
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[i] + nums[j] + nums[k - 1] > target:
                        break;
                    if k < len(nums) - 1 and nums[i] + nums[j] + nums[k + 1] < target:
                        continue;
                    if nums[i] + nums[j] + nums[k] == target:
                        return target;
                    if abs(out - target) > abs(nums[i] + nums[j] + nums[k] - target):
                        out = nums[i] + nums[j] + nums[k];
        return out;