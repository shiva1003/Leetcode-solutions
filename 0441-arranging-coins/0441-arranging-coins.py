class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        h=n
        res=1
        while l< h:
            mid = (l+h)//2
            coin = (float(mid)/2)*(mid+1) 
            if coin > n:
                h = mid
            else:
                l = mid+1
                res=max(mid, res)
        return res