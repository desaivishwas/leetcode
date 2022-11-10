class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        res = []
        for i in range(1, len(arr)):
            x = abs(arr[i] - arr[i-1])
            min_diff = min(min_diff, x)
            
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])
        return res
            