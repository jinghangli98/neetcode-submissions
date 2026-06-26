class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        seen = []
        for token in tokens:
            
            if token == "+":
                recent, earlier = seen.pop(), seen.pop()
                seen.append(recent + earlier)
            
            elif token == "-":
                recent, earlier = seen.pop(), seen.pop()
                seen.append(earlier - recent)
            
            elif token == "/":
                recent, earlier = seen.pop(), seen.pop()
                seen.append(int(earlier/recent))
            
            elif token == "*":
                recent, earlier = seen.pop(), seen.pop()
                seen.append(int(earlier * recent))
            else:
                seen.append(int(token))
        
        return seen[0]


