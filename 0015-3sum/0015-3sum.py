class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        arr = sorted(arr)
        result = []
        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            while k > j:
                sum = arr[i] + arr[j] + arr[k]
                target = 0
                if sum == target:
                    result.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1
                    while j < k and arr[j] == arr[j - 1]:
                            j += 1
                elif sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                        
        return result           
