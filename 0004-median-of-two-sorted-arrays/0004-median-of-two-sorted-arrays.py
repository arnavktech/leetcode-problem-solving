class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = sorted(nums1 + nums2)
        n = len(arr)

        mid = n // 2

        if n % 2 != 0:
            return arr[mid]
        elif n % 2 == 0:
            return (arr[mid-1] + arr[mid]) / 2