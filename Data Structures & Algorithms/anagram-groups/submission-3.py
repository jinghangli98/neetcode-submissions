class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for substring in strs:
            key = ''.join(sorted(substring))
            if key in table:
                table[key].append(substring)
            else:
                table[key] = [substring]

        return [val for key, val in table.items()]
