class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for idx, sub_str in enumerate(strs):
            sorted_sub_str = ''.join(sorted(sub_str))
            if sorted_sub_str in ans:
                ans[sorted_sub_str].append(sub_str)
            else:
                ans[sorted_sub_str] = [sub_str]
        
                
        return ([val for key, val in ans.items()])