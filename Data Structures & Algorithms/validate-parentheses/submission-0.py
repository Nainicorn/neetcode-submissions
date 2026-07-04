class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'[':']', '{':'}', '(':')'}
        stack = []
        for c in s:
            if c in chars:
                stack.append(c)
            else:
                # if it doesnt have corresponding char 
                if not stack or chars[stack[-1]] != c:
                    return False
                stack.pop()

        # if stack is empty then true, but if not then false
        return not stack
            