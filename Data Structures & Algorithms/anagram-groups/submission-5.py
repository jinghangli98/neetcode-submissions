class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        for sub_str in strs:
            key = ''.join(sorted(sub_str))
            if key in table:
                table[key].append(sub_str)
            else:
                table[key] = [sub_str]
        
        return [value for key, value in table.items()]