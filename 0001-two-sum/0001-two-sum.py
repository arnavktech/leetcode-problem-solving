class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = sorted((num, idx) for idx, num in enumerate(nums))

        i, j = 0, len(arr) - 1

        while i < j:
            total = arr[i][0] + arr[j][0]

            if total == target:
                return [arr[i][1], arr[j][1]]
            elif total < target:
                i += 1
            else:
                j -= 1