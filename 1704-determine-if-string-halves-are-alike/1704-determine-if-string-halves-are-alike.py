class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s= s.lower()
        n = len(s)//2
        v = "aeiou"
        a = s[:n]
        b = s[n:]
        s1 = sum(ch in v for ch in a)
        s2 = sum(ch in v for ch in b)
        return s1 == s2