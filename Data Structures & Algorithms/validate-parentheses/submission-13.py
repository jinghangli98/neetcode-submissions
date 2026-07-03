class Solution:
    def isValid(self, s: str) -> bool:
        
        lut = {"]":"[", "}": "{", ")":"("}

        stack = []
        for item in s:
            if item in lut:
                #closing
                if stack and stack[-1] == lut[item]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(item)
        
        return len(stack) == 0
