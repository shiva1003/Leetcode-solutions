class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l=len(arr)
        for i in range (l):
            for j in range(l):
                if i!=j and arr[i] == 2 * arr[j]:
                    return True
        return False
        