class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == "+":
                recent = stack.pop()
                prev = stack.pop()
                
                stack.append(prev + recent)

            elif token == "-":
                recent = stack.pop()
                prev = stack.pop()
                
                stack.append(prev - recent)
            
            elif token == "*":

                recent = stack.pop()
                prev = stack.pop()
                
                stack.append(prev * recent)

            elif token == "/":

                recent = stack.pop()
                prev = stack.pop()
                
                stack.append(int(prev / recent))
            
            else:
                stack.append(int(token))
        
        return stack[0]