class Solution:
    def isValid(self, s: str) -> bool:
        
        table = {"}":"{", ")":"(", "]":"["}

        stack = []
        for b in s:
            
            if b not in table:
                stack.append(b)
            else:
                #closing bracket
                if stack and stack[-1] == table[b]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0