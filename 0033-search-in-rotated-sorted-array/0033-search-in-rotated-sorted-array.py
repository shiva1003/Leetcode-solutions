class Solution:
    def search(self, n: List[int], target: int) -> int:
        l = 0  
        h = len(n)-1
        while l <= h:
            mid=(l+h)//2   
            if n[mid] == target:
                return mid
            elif n[mid] >= n[l]:
                if (target >= n[l] and target < n[mid]):
                    h = mid-1
                else:
                    l = mid+1
            else:
                if (target <=n [h] and target > n[mid]):
                    l = mid+1
                else:
                    h = mid-1
        return -1
        