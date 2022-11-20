class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        n = len(arr)
        w_sum = sum(arr[:k])
        max_avg = w_sum
        for ele in range(1, n-k+1):
            w_sum -= arr[ele-1]
            w_sum += arr[ele+k-1]
            max_avg = max(max_avg, w_sum)
        return max_avg / k