# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 0, n-1
        while l<=h:
            mid = l+(h-l)//2
            if isBadVersion(mid) == False :
                l = mid+1
            else:
                h = mid-1
        return l
