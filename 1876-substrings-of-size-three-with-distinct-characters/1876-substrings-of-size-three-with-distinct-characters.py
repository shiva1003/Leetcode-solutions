class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        wstart = wend = 0
        l=[]
        count=0

        while wend < len(s):
            l.append(s[wend])
            if wend-wstart+1 < k :
                wend += 1
            elif wend - wstart + 1 == k:
                new_l=set(l)
                if len(new_l) == k:
                    count+=1

                l.remove(s[wstart])
                wstart += 1
                wend += 1
        return count
        