class Solution:
    def isValid(self, s: str) -> bool:
        
        #iterate through the string, if it's an closing bracket see if the last bracket in the stack is a matching pair, then pop the stack
        #if it's an open bracekt then append in the stack
        table = {")":"(", "}":"{", "]":"["}
        stack = []
        for b in s:
            if b in table:
                if stack and stack[-1] == table[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0
        


            