class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n+1):
            count = 0
            for j in range(n):
                if nums[j] >= i:
                    count += 1
            if count == i:
                return i
        return -1
