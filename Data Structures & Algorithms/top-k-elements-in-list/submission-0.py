class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        
        sorted_dict = dict(sorted(table.items(), key=lambda item: item[1], reverse=True))
        ans = []
        idx = 0
        for key, val in sorted_dict.items():
            if idx < k:
                ans.append(key)
                idx += 1
            else:
                break
        
        return ans


