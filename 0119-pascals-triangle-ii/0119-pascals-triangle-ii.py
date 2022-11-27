class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans =[]
        for i in range(rowIndex+1):
            for j in range(i+1):
                ans.append([])
                if j==0:
                    ans[i].append(1)
                elif i==j :
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1]+ans[i-1][j])
        return ans[rowIndex]
        
        