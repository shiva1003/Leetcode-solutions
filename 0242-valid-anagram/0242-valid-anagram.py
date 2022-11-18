class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1, str2 = {}, {}
        for i in s:
            if i in str1:
                str1[i] += 1
            else:
                str1[i] = 1
        for i in t:
            if i in str2:
                str2[i] += 1
            else:
                str2[i] = 1
        return (str1 == str2 and len(s) == len(t))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       