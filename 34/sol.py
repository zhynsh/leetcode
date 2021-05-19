#https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0;
        end = len(nums);
        sol = [-1, -1];
        def bsl(begin: int, end: int):
            if begin >= end:
                return -1;
            mid = int((begin + end) / 2);
            if nums[mid] > target:
                return bsl(begin, mid);
            if nums[mid] < target:
                return bsl(mid + 1, end);
            if nums[mid] == target:
                if mid == 0 or nums[mid] > nums[mid - 1]:
                    return mid;
                else:
                    return bsl(begin, mid);
        def bsr(begin: int, end: int):
            if begin >= end:
                return -1;
            mid = int((begin + end) / 2);
            if nums[mid] > target:
                return bsr(begin, mid);
            if nums[mid] < target:
                return bsr(mid + 1, end);
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                    return mid;
                else:
                    return bsr(mid + 1, end);
        sol[0] = bsl(0, len(nums));
        sol[1] = bsr(0, len(nums));
        return sol;
