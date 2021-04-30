class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1);
        n = len(nums2);
        for i in range(0, len(nums2)):
            nums1.append(nums2[i]);
        nums1.sort();
        if (m + n) % 2 == 0:
            return 1.0 * (nums1[int((m + n) / 2)] + nums1[int((m + n) / 2) - 1]) / 2;
        else:
            return nums1[int((m + n - 1) / 2)];