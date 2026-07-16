class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == "+":
                old, recent = stack.pop(), stack.pop()
                stack.append(int(old + recent))
            elif token == "-":
                old, recent = stack.pop(), stack.pop()
                stack.append(int(recent - old))
            elif token == "/":
                old, recent = stack.pop(), stack.pop()
                stack.append(int(recent/old))
            elif token == "*":
                old, recent = stack.pop(), stack.pop()
                stack.append(int(old * recent))

            else:
                stack.append(int(token))
        
        return stack[-1]