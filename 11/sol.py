class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0;
        left = 0;
        right = len(height) - 1;
        leftmax = height[left];
        rightmax = height[right];
        while left < right:
            if height[left] < leftmax:
                left = left + 1;
                continue;
            if height[right] < rightmax:
                right = right - 1;
                continue;
            leftmax = height[left];
            rightmax = height[right];
            if out < min(height[left], height[right]) * (right - left):
                out = min(height[left], height[right]) * (right - left);
            if height[left] < height[right]:
                left = left + 1;
            else:
                right = right - 1;
        return out;