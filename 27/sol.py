class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        jump = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                jump = jump + 1;
                nums[jump] = nums[i];
        return jump + 1;