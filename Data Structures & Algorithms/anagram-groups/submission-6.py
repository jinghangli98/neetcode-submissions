class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        for substr in strs:
            key = "".join(sorted(substr))
            if key in table:
                table[key].append(substr)
            else:
                table[key] = [substr]
        
        return [values for key, values in table.items()]