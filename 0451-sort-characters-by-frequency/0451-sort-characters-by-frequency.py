class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        sorted_s = sorted(a.items(), key = lambda x:x[1], reverse = True)
        res=''
        for i in sorted_s:
                res+=i[0]*i[1]
        return res

