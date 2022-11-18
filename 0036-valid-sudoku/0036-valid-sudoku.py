class Solution:
    def isValidSudoku(self, box: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sq = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if box[r][c] == ".":
                    continue
                if (box[r][c] in rows[r] or box[r][c] in cols[c] or box[r][c] in sq[(r//3, c//3)]):
                    return False
                cols[c].add(box[r][c])
                rows[r].add(box[r][c])
                sq[(r//3, c//3)].add(box[r][c])
        return True
                
                
        
        