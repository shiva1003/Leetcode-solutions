class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=0
        r = len(num)-1
        while l<=r:
            if (num[l]+num[r]) == target:
                return (l+1, r+1)
            if (num[l]+num[r]) > target :
                r-=1
            else: 
                l += 1
                    
        