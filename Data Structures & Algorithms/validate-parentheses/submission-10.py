class Solution:
    def isValid(self, s: str) -> bool:
        lut = {']':'[', '}':'{', ")":"("}

        stack = []

        for b in s:
            if b not in lut:
                #open b
                stack.append(b)
            else:
                #closed b
                if stack and stack[-1] == lut[b]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0