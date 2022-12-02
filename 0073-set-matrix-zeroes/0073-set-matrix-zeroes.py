class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        R = len(m)
        C = len(m[0])
        r = set()
        c = set()
        for i in range(R):
            for j in range(C):
                if m[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(R):
            for j in range(C):
                if i in r or j in c:
                    m[i][j]=0
        return m
        