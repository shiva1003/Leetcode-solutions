class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans =[]
        for i in range(numRows):
            ans.append([])
            for j in range(i+1):
                if i==j:
                    ans[i].append(1)
                elif j==0:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        return ans