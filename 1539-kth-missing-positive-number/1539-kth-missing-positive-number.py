class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """l=[]
        for i in range(0, (arr[-1]+k)+1):
            l.append(i)
            sdif = set(l).symmetric_difference(set(arr))  one test case was not passing with this code
            temp_list=list(sdif)
        return (temp_list[k])"""
        
        l = 0
        h = len(arr)-1
        while l <= h:
            mid = (l+h)//2
            missed = arr[mid] - (mid+1)
            if missed < k:
                l = mid+1 
            else :
                h = mid-1
        return l+k
        
        