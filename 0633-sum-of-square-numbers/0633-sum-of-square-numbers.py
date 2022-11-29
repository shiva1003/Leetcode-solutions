class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, h =0, math.floor(c**0.5)
        while l <= h:
            if l**2 + h**2 == c:
                return True
            elif l**2 + h**2 < c:
                l += 1
            else:
                h -= 1
        return False

        