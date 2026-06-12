class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        for l in range(len(s2) + 1 -len(s1)):
            check_s2 = s2[l:l+len(s1)]
            if self.checkpermutation(s1, check_s2):
                return True
        
        return False
        
    
    def checkpermutation(self, s1: str, s2:str) -> bool:

        s1_table = {}
        s2_table = {}

        for s in s1:
            if s in s1_table:
                s1_table[s] += 1
            else:
                s1_table[s] = 1
        
        for s in s2:
            if s in s2_table:
                s2_table[s] += 1
            else:
                s2_table[s] = 1
        
        return s1_table == s2_table
    
