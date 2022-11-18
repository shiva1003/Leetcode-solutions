class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # if it's the left bracket then we append it to the stack
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # or if it is empty or left is not there
                return False
        return len(stack) == 0 # finally check if the stack still contains unmatched left bracket
	


        