class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0] :
            return letters[0]
        
        lo, hi = 0, len(letters)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if target >= letters[mid]:
                lo = mid+1
            elif target < letters[mid]:
                hi = mid-1
            else:
                return mid
            
        return letters[lo]
  