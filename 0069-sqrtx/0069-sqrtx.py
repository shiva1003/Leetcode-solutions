class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l<=h:
            mid = (l+h)//2
            if mid**2 < x:
                l = mid+1
            elif mid**2 > x:
                h = mid-1
            else:
                return mid
        return h
        
        