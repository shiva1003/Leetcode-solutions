class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = res = nums[0]
        for i in nums[1:] : # here we are accessing the value directly with nums[1:]
            currMax = max(max_p * i, min_p * i, i) #tuple packing 
            currMin = min(max_p * i, min_p * i, i)
            max_p = currMax
            min_p = currMin
            res = max(res, max_p)
        
        return res