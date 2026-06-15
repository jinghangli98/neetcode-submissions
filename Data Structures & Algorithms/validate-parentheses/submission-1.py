class Solution:
    def isValid(self, s: str) -> bool:
        
        lut = {']':'[', ')':'(', '}':'{'}
        openb = []
        for b in s:
            if b in lut: #if it's a closing bracket
                if openb and openb[-1] == lut[b]:
                    openb.pop()
                else:
                    return False
            else:
                openb.append(b)
        
        if len(openb) == 0: 
            return True
        else:
            return False