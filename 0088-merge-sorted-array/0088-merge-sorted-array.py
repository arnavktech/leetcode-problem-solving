class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        sum = nums1[:m] + nums2[:n]
        sum = sorted(sum)
        nums1[:] = sum
            

        
        