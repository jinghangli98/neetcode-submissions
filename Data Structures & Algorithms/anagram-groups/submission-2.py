class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            if ''.join(sorted(string)) in ans:
                ans[''.join(sorted(string))].append(string)
                
            else:
                ans[''.join(sorted(string))] = [string]
        
        return [val for key, val in ans.items()]