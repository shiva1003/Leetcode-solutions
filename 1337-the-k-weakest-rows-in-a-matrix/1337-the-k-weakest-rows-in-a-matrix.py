class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        for i, x in enumerate(mat):
            a = (sum(x),i)
            temp.append(a)
        temp.sort()
        return [i[1] for i in temp[:k]]
        
        
       